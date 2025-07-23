from django.shortcuts import render
from django.http import HttpResponse

def stats(request):
    return render(request, 'stats.html')

#class stats_view(View):
#    def stats(self, request):
#        stats = NpcStatistics.objects.all()
#        return render(request, 'stats.html', context={'stats':stats})

