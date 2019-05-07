from django.contrib.auth.models import User, Group
from django.db.models import signals
from django.db.models.signals import post_save
from rest_framework import serializers
from webapp.models import *
from webapp import signals
from phonenumber_field.serializerfields import PhoneNumberField

class ClientSerializer(serializers.ModelSerializer):
    tel = PhoneNumberField(required = True)
    loyalty = serializers.FloatField(read_only = True)
    #address = serializers.CharField(required = True)
    class Meta:
        model = Clients
        fields = ('tel','loyalty',)

class SellerSerializer(serializers.ModelSerializer):
    epon = serializers.CharField(required = True)
    title = serializers.CharField(required = True)
    afm = serializers.CharField(required = True)
    #adress = serializers.CharField(required = True)
    city = serializers.CharField(required = True)
    tel = PhoneNumberField(required = True)
    occupation = serializers.CharField(required = True)
    class Meta:
        model = Sellers
        fields = ('tel', 'epon', 'title', 'afm', 'city', 'occupation')

class AddressSerializer(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required = False)
    title = serializers.CharField(required = True)
    address = serializers.CharField(required = True)
    doorbell = serializers.CharField(required = False)
    number = serializers.IntegerField(required = False)
    class Meta:
        model = Address
        fields = '__all__'

class UserSerializer(serializers.HyperlinkedModelSerializer):
    groups = serializers.CharField()
    profile = serializers.CharField()
    email = serializers.EmailField(required = True)
    #address = AddressSerializer(many=True, required = False)
    class Meta:
        model = User
        fields = ('username', 'email', 'groups', 'first_name', 'last_name', 'password', 'profile')

    def validate_groups(self, value):
        """
        Check that the blog post is about Django.
        """
        available_groups = ['client', 'seller']
        if not any(group in value.lower() for group in available_groups):
            raise serializers.ValidationError("Group Error")
        return value

    def validate(self, data):
        """
        Check that the blog post is about Django.
        """
        print("MPHKA")
        group = data.get('groups')
        print(group)
        if(group == 'client'):
            print(data.get('profile')['tel'])
            if(len(Clients.objects.filter(tel=data.get('profile')['tel'])) > 0):
                raise serializers.ValidationError({'error_message': ['A user with this telephone already exists.']})
        #available_groups = ['client', 'seller']
        #if not any(group in value.lower() for group in available_groups):
        #    raise serializers.ValidationError("Group Error")
        return data

    def create(self, validated_data):
        gr = validated_data.pop('groups')
        if validated_data.get('profile'):
            profile_data = validated_data.get('profile')
            if(gr == 'client'):
                profile_serializer = ClientSerializer(data=profile_data)
                if profile_serializer.is_valid():
                    validated_data['profile'] = profile_data
            elif(gr == 'seller'):
                profile_serializer = SellerSerializer(data=profile_data)
                if profile_serializer.is_valid():
                    validated_data['profile'] = profile_data
        #user = super(UserSerializer, self).create(validated_data) kept for versioning
        user = User.objects.create(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.email = validated_data['email']
        user.first_name = validated_data['first_name']
        user.last_name = validated_data['last_name']
        #for addr in validated_data['address']:
        #    Address.objects.create(user_id = user, **addr)
        group = Group.objects.get(name=gr)
        user.groups.add(group)
        user.save()
        signals.user_created.send(sender = User, instance = user, created = True, data = validated_data['profile'])
        return user

    def __init__(self, *args, **kwargs):
        super(UserSerializer, self).__init__(*args, **kwargs)
        #request = kwargs['context']['request']
        print(repr(args))
        if(kwargs.get('data')):
            group = kwargs['data']['groups']
            profile = kwargs['data']['profile']
        else:
            print(args[0].profile.category)
            group = args[0].profile.category
            if group == 'client':
                args[0].profile = Clients.objects.get(user_id = args[0].id)
            else:
                args[0].profile = Sellers.objects.get(user_id = args[0].id)
        if group == 'client':
            self.fields['profile'] = ClientSerializer(required = True)
        elif group == 'seller':
            self.fields['profile'] = SellerSerializer(required = True)


class CategorySerializer(serializers.ModelSerializer):
    cid = serializers.IntegerField(read_only=True)
    parent_name = serializers.CharField(required = False)
    parent_cid = serializers.PrimaryKeyRelatedField(queryset=Categories.objects.all(),required=False)
    class Meta:
        model = Categories
        fields = ('cid', 'name', 'parent_cid','parent_name',)

    def validate(self, data):
        """
        Check that the parent category exists.
        """
        if data.get('parent_name') and data.get('parent_cid'):
            raise serializers.ValidationError({'parent_cid': ["Cannot give both id and name in parent category"]})
        elif data.get('parent_name'):
            parent_category = Categories.objects.filter(name__iexact = data.get('parent_name'))
            if len(parent_category)<=0:
                raise serializers.ValidationError({'parent_name': ["Parent Category does not exist"]})
            parent_category = Categories.objects.get(name__iexact = data.get('parent_name'))
            data['parent_cid'] = parent_category
            data.pop('parent_name')
        return data

class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(required = False)
    price = serializers.FloatField(min_value = 0)
    loyalty = serializers.FloatField(min_value = 0)
    description = serializers.CharField(required = False)
    double_price_mod = serializers.FloatField(min_value = 0, required = False)
    PID = serializers.IntegerField(read_only=True)
    class Meta:
        model = Products
        fields = ('PID', 'name','cid','price','category_name','loyalty','description','double_price_mod','enabled','image',)

    def validate(self, data):
        """
        Check that the product category exists.
        """
        if data.get('category_name') and data.get('cid'):
            raise serializers.ValidationError({'category_cid': ["Cannot give both id and name in product category"]})
        elif data.get('category_name'):
            product_category = Categories.objects.filter(name__iexact = data.get('category_name'))
            if len(product_category)<=0:
                raise serializers.ValidationError({'category_name': ["Product Category does not exist"]})
            product_category = Categories.objects.get(name__iexact = data.get('category_name'))
            data['cid'] = product_category
            data.pop('category_name')
        elif not data.get('cid'):
            raise serializers.ValidationError({'category_cid': ["No Category Provided"]})
        return data

class ChoiceSerializer(serializers.ModelSerializer):
    price_mod = serializers.FloatField(min_value = 0, required = False)
    class Meta:
        model = Choices
        fields = ('choice','price_mod',)

class ValueSerializer(serializers.ModelSerializer):
    #value = serializers.CharField(required = True)
    class Meta:
        model = Values
        fields = ('value',)

class AttributeSerializer(serializers.ModelSerializer):
    aid = serializers.PrimaryKeyRelatedField(read_only=True)
    category_name = serializers.CharField(required = False)
    choices = ChoiceSerializer(many = True, required = False)
    values = ValueSerializer(many = True, required = False)
    class Meta:
        model = Attributes
        fields = ('name','choices','values','category_name','cid','ordering','aid',)

    def validate(self, data):
        """
        Check that the product category exists.
        """
        if data.get('category_name') and data.get('cid'):
            raise serializers.ValidationError({'category_cid': ["Cannot give both id and name in product category"]})
        elif data.get('category_name'):
            product_category = Categories.objects.filter(name__iexact = data.get('category_name'))
            if len(product_category)<=0:
                raise serializers.ValidationError({'category_name': ["Product Category does not exist"]})
            product_category = Categories.objects.get(name__iexact = data.get('category_name'))
            data['cid'] = product_category
            data.pop('category_name')
        elif not data.get('cid'):
            raise serializers.ValidationError({'category_cid': ["No Category Provided"]})
        #if not data.get('values'):
        #    raise serializers.ValidationError({'Values': ["No values were provided for the attribute"]})
        return data

    def create(self, validated_data):
        print("Att Create")
        if Attributes.objects.filter(name__iexact = validated_data.get('name'), cid = validated_data.get('cid')):
            raise serializers.ValidationError({'name': ["Not unique category name and category id"]})
        attr = Attributes.objects.create(name=validated_data['name'])
        attr.cid = validated_data['cid']
        if validated_data.get('values'):
            values_data = validated_data.pop('values')
            for value_data in values_data:
                Values.objects.create(attr=attr, **value_data)
        if validated_data.get('choices'):
            choices_data = validated_data.pop('choices')
            for choice_data in choices_data:
                Choices.objects.create(attr=attr, **choice_data)
        attr.save()
        return attr

    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        choices_data = validated_data.pop('choices')
        values_data = validated_data.pop('values')
        choices = (instance.choices).all()
        #choices = list(choices)
        choices.delete()
        values = (instance.values).all()
        values.delete()
        #values = list(values)
        instance.save()
        for choice_data in choices_data:
            #choice = choices.pop(0)
            #print(choice.choice)
            #print(choice_data.get('choice'))
            #choice.choice = choice_data.get('choice')
            #choice.save()
            Choices.objects.create(attr=instance,**choice_data)
        for value_data in values_data:
            #if(len(values) > 0):
                #value = values.pop(0)
                #value.value = value_data.get('value', value.value)
                #value.save()
            Values.objects.create(attr=instance,**value_data)
        return instance

class FavAttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fav_Attributes
        fields = ('slidervalue', 'choiceindex', 'headline', 'attr')

class FavProductSerializer(serializers.ModelSerializer):
    attributes = FavAttributeSerializer(many = True)
    prod = ProductSerializer(source = 'pid', read_only=True)
    cat = CategorySerializer(source = 'cid', read_only=True)
    price = serializers.FloatField()
    fpid = serializers.PrimaryKeyRelatedField(read_only=True)
    comments = serializers.CharField(allow_blank = True)
    class Meta:
        model = Fav_Products
        fields = ('fpid', 'count', 'price', 'product', 'category', 'prod', 'cat', 'attributes', 'comments',)

class FavouritesSerializer(serializers.ModelSerializer):
    products = FavProductSerializer(many = True)
    class Meta:
        model = Favourites
        fields = ('uid', 'products')

    def create(self, validated_data):
        (favourite, created) = Favourites.objects.get_or_create(uid = validated_data['uid'])
        produ = validated_data['products']
        for prod in produ:
            pr = Products.objects.get(name = prod.get('product'))
            ca = Categories.objects.get(name = prod.get('category'))
            attributes = prod.pop('attributes')
            pr1 = Fav_Products.objects.create(fid=favourite, pid = pr, cid = ca, **prod)
            for attribute in attributes:
                Fav_Attributes.objects.create(fpid = pr1, **attribute)
        favourite.save()
        return pr1


class OrderAttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order_Attributes
        fields = ('slidervalue', 'choiceindex', 'headline', 'attr')

class OrderProductSerializer(serializers.ModelSerializer):
    attributes = OrderAttributeSerializer(many = True)
    prod = ProductSerializer(source = 'pid', read_only=True)
    cat = CategorySerializer(source = 'cid', read_only=True)
    price = serializers.FloatField()
    opid = serializers.PrimaryKeyRelatedField(read_only=True)
    comments = serializers.CharField(allow_blank = True)
    class Meta:
        model = Order_products
        fields = ('opid', 'count', 'price', 'product', 'category', 'prod', 'cat', 'attributes', 'comments',)

class OrdersSerializer(serializers.ModelSerializer):
    products = OrderProductSerializer(many = True)
    oid = serializers.PrimaryKeyRelatedField(read_only=True)
    addr_description = serializers.CharField(allow_blank = True, required = False,allow_null=True)
    area = serializers.CharField(allow_blank = True, required = False)
    floor = serializers.CharField(allow_blank = True, required = False,allow_null=True)
    internal_number = serializers.CharField(allow_blank = True, required = False,allow_null=True)
    doorbell = serializers.CharField(allow_blank = True, required = False,allow_null=True)
    datetime = serializers.DateTimeField(read_only=True)
    class Meta:
        model = Orders
        fields = ('uid', 'products', 'oid', 'price', 'loyalty','email','first_name','last_name','telephone','address','number','tax_kod','floor','internal_number','doorbell','addr_description','datetime','area')

    def create(self, validated_data):
        produ = validated_data.pop('products')
        order = Orders.objects.create(**validated_data)

        for prod in produ:
            pr = Products.objects.get(name = prod.get('product'))
            ca = Categories.objects.get(name = prod.get('category'))
            attributes = prod.pop('attributes')
            pr1 = Order_products.objects.create(oid=order, pid = pr, cid = ca, **prod)
            for attribute in attributes:
                Order_Attributes.objects.create(opid = pr1, **attribute)
        order.save()
        return order
