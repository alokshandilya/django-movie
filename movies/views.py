from django.shortcuts import render


# Create your views here.
def index(request):
    return render(
        request,
        "movies/index.html",
        context={
            "movies": [
                "the matrix",
                "the matrix reloaded",
                "the matrix revolutions",
            ],
        },
    )


def about(request):
    return render(request, "movies/about.html")
