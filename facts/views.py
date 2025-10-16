from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Fact
from .serializers import FactSerializer
import random # Add this import

@api_view(['GET'])
def random_fact_view(request):
    """
    Retrieves a random fact from the database.
    """
    count = Fact.objects.count()
    if count == 0:
        return Response({'detail': 'No facts available.'}, status=status.HTTP_404_NOT_FOUND)
    
    random_index = random.randint(0, count - 1)
    fact = Fact.objects.all()[random_index]
    serializer = FactSerializer(fact)
    return Response(serializer.data)

@api_view(['GET'])
def search_facts_view(request):
    """
    Searches facts by a query string.
    """
    query = request.GET.get('q', '')
    if not query:
        return Response({'detail': 'Please provide a search query.'}, status=status.HTTP_400_BAD_REQUEST)
    
    facts = Fact.objects.filter(text__icontains=query)
    serializer = FactSerializer(facts, many=True)
    return Response(serializer.data)

#from rest_framework.response import Response
#from rest_framework.decorators import api_view
#from .helpers import get_random_fact
#from .models import Fact
#from .serializers import FactSerializer
#api_view(['GET'])
#def randon_fact_view(request):
    #fact_text = get_random_fact()

    #fact = Fact.objects.create(text=fact_text)
    #serializer = FactSerializer(fact)
    #return Response(serializer.data)

