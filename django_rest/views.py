from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from recipeapp.models import *
from rest_framework.views import APIView
from recipeapp.serializers import RecipeSerializer

@api_view(["GET", "POST"])
def index(request):

    if request.method == "POST":
        print(request.POST)
        return Response(data = {
            "message" : "Thankyou"
        }
        )
    data = [
        {"id": 1, "name": "John"},
        {"id": 2, "name": "Jane"},
    ]

    my_dict = {
        "message": "Hello, World!",
    }
    return Response(data=data)

@api_view(['GET','POST'])
def recipe(request):
    'this is recipe list view'
    reciepes = Recipe.objects.all()
    serializer = RecipeSerializer(reciepes, many = True)
    if request.method == 'POST':
        serializer= RecipeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status = 201, data=serializer.data)
        # return Response(status=400, data=serializer.errors)
    return Response(data=serializer.data)


@api_view(['GET','PUT', 'DELETE'])
def recipe_detail(request, id):
    'this is recipe detail view'

    try:
        recipe = Recipe.objects.get(id=id)
    except:
        return Response(status = 404 ,data={ "message": "Recipe not found"})
    recipe = Recipe.objects.get(id=id)
    if request.method == "PUT":
        serializer = RecipeSerializer(instance = recipe, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data)

    if request.method == "DELETE":
        recipe.delete()
        return Response(status=204, data= True)
    

    serializer = RecipeSerializer(recipe)
    return Response(data=serializer.data)







class RecipeView(APIView):
    def get(self, request):
        recipes = Recipe.objects.all()
        serializer = RecipeSerializer(recipes, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = RecipeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=201, data=serializer.data)
    

class RecipeDetailView(APIView):
    def get(self, request, id):
        try:
            recipe = Recipe.objects.get(id=id)
        except Recipe.DoesNotExist:
            return Response(status = 404 ,data={ "message": "Recipe not found"})
        serializer = RecipeSerializer(recipe)
        return Response(serializer.data)
    
    def put(self, request, id):
        try:
            recipe = Recipe.objects.get(id=id)
        except Recipe.DoesNotExist:
            return Response(status = 404 ,data={ "message": "Recipe not found"})
        serializer = RecipeSerializer(instance=recipe, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=200, data=serializer.data)
    
    def delete(self, request, id):
        try:
            recipe = Recipe.objects.get(id=id)
        except Recipe.DoesNotExist:
            return Response(status = 404 ,data={ "message": "Recipe not found"})
        recipe.delete()
        return Response(status=204, data= None)
    
