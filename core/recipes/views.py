from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Recipe
from .serializers import RecipeSerializer


@api_view(['GET', 'POST'])
def recipe_list_create(request):
    if request.method == 'GET':
        recipes = Recipe.objects.all()
        serializer = RecipeSerializer(recipes, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = RecipeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def recipe_detail(request, pk):
    try:
        recipe = Recipe.objects.get(pk=pk)
    except Recipe.DoesNotExist:
        return Response({"error": "Recipe not found"}, status=404)
    
    if request.method == 'GET':
        serializer = RecipeSerializer(recipe)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = RecipeSerializer(recipe, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    if request.method == 'DELETE':
        recipe.delete()
        return Response(status=204)
    

@api_view(['GET'])
def sample_recipe(request):
    data = [
        {
            "id": 1,
            "title": "Spicy Indian Curry",
            "description": "A hot and spicy traditional Indian curry",
            "ingredients": "Onion, tomato, chili, garam masala, chicken",
            "cook_time": 30
        },
        {
            "id": 2,
            "title": "Paneer Butter Masala",
            "description": "Creamy tomato based paneer curry",
            "ingredients": "Paneer, butter, tomato, cream, cashew",
            "cook_time": 25
        },
       
    ]
    return Response(data, status=status.HTTP_200_OK)