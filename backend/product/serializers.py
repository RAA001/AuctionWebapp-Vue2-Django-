from rest_framework import serializers

from .models import Category, Product,Questions,Answers,Profile,Bids

"""Product serializer, ensures products can be fetched from frontend"""
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "description",
            "price",
            "get_image",
            "get_thumbnail",
            'date_finish',
            "user",
            'email'
            
        )
"""Categories serializer, ensures categories can be fetched from frontend"""
class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = Category
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "products",
        )


"""Create Product serializer, ensures products can be deployed from frontend"""
class CreateProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        category = serializers.StringRelatedField()
        fields = (
            "id",
            "category",
            "name",
            "slug",
            "description",
            "price",
            "image",
            "date_added",
            "date_finish",
            "get_image",
            "get_thumbnail",
            'user',
            'email'

        )
"""Create Question serializer, ensures questions about products can be seen by everyone and answered appropriately"""
class CreateQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = [
            "id",
            "title",
            "product",
            "user",
            "question",


        ]
"""Create Answer Serializer ensures that answers can be posted in relation to questions"""
class CreateAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answers
        fields = (
            "id",
            "product",
            "user",
            'question',
            "answer",
        )
"""Get Profile Serializer fetches the user who is logged in in the view function, this simply transfers the data as an api"""
class GetProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model=Profile
        fields = (
            "id",
            "username",
            "email",
            'first_name',
            "last_name",
            "image",
            "dOB",
            "phoneNumber",
            "addressLine1",
            "addressLine2",
            "city",
            "postcode",
            "country",
            "get_image"
        )

"""Get bids serializer will fitch bids, and post bids based on the product id"""
class GetBidsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Bids
        
        fields = (
            "id",
            "user",
            "price",           
            "product",
            "date_added"
        )

"""This serializer is used to simply update user info"""
class GetProfileSerializer1(serializers.ModelSerializer):

    class Meta:
        model=Profile
        
        fields = (
            "id",

            "username",

            'first_name',
            "last_name",
            "email",
            "dOB",
            "phoneNumber",
            "addressLine1",
            "addressLine2",
            "city",
            "postcode",
            "country",
            "get_image"
        )

"""This serializer can be used to transfer image data to the backend"""
class GetImageSerializer(serializers.ModelSerializer):

    class Meta:
        model=Profile
        fields = (
            "id",
            "image",
            "get_image"
        )