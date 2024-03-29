from django.urls import path

from .views import (
            inicio,
            registro,
            loginView,
            logout_vista,
            HomeUsuario,
            jugar,
            resultado_pregunta,
            tablero
            )

urlpatterns = [

  path("inicio/", inicio, name="inicio"),
  path("HomeUsuario/", HomeUsuario, name="HomeUsuario"),
  path("login/", loginView, name="login"),
  path("logout/", logout_vista, name="logout"),
  path("registro/", registro, name="registro"),
  path("tablero/", tablero, name="tablero"),
  path("jugar/", jugar, name="jugar"),
  path("resultado/<int:pregunta_respondida_pk>/", resultado_pregunta, name="resultado"),
]