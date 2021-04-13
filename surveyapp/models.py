from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)


author = 'Samuel D. Restrepo'

doc = """
Esta es una encuesta interactiva que realiza intervenciones
"""


class Constants(BaseConstants):
    name_in_url = 'surveyapp'
    players_per_group = None
    num_rounds = 1

class Subsession(BaseSubsession):

    def creating_session(subsession):

        import itertools
        import random
        import string
        from random import choice
        from string import ascii_lowercase, digits
        #Creamos una lista
        list_tratam = [0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3]
        #Aleatorizamos la lista
        random.shuffle(list_tratam)
        #Iniciamos ciclos para balancear los tratamientos
        tratamiento = itertools.cycle(list_tratam)
        chars = ascii_lowercase + digits
        labels = [''.join(choice(chars) for _ in range(7)) for _ in range(1500)]
        for player, label in zip(subsession.get_players(), labels):
            player.participant.label = label
            player.label = label
            #Finalizamos ciclos para que los tratamientos queden balanceados
            player.tratamiento = next(tratamiento)
            #Aleatorización simple para las figuras (esta aleatorización es independiente una de la otra e independiente del esquema de aleatorización de los tratamientos)
            player.ideal_s = random.choice([1,2,3,4])
            player.percepciones_s = random.choice([2,3,4,5])
            # Aleatorización de códigos para finalizar la encuesta mturk
            player.completion_codes = random.randint(100000,999999)



class Group(BaseGroup):
    pass


class Player(BasePlayer):
    label = models.StringField()
    #Variable para guardar el ID del trabajador Prolific
    prolific_id = models.StringField(label="")
    #Variable para guardar el código aleatorizado mturk
    completion_codes = models.IntegerField()
    ### Variables para guardar los tratamientos aleatorizados e imágenes aleatorizadas de sociedades
    tratamiento = models.IntegerField()
    ideal_s = models.IntegerField()
    percepciones_s = models.IntegerField()
    ### Preguntas socio-demográficas
    participa = models.BooleanField(label = "",
        choices=[[True,'Sí, me gustaría contestar la encuesta, y confimo que soy un RESIDENTE PERMANENTE DE MÉXICO y tengo más de 18 años'],[False, 'No, prefiero no participar']]
                                )

    edad = models.PositiveIntegerField(label="",
                                       min=0, max=100,
                                      )
    sexo = models.IntegerField(label="",
                                choices=[
                                    [1, "Hombre"],
                                    [2, "Mujer"],
                                     ],
                               widget=widgets.RadioSelectHorizontal,
                               blank=True
                                )
    es_civil = models.IntegerField(label="",
                                        choices=[
                                            [1,"Casado"],
                                            [2, "Soltero"],
                                            [3, "Unión libre"],
                                            [4, "Separado/Divociado"],
                                            [5, "Viudo"],
                                             ],
                                        blank = True
                                        )
    nacimiento = models.IntegerField(label="",
                                   choices=[
                                       [1, "Aguascalientes"],
                                       [2, "Baja California"],
                                       [3, "Baja California Sur"],
                                       [4, "Campeche"],
                                       [5, "Coahuila de Zaragoza"],
                                       [6, "Colima"],
                                       [7, "Chiapas"],
                                       [8, "Chihuahua"],
                                       [9, "Distrito Federal"],
                                       [10, "Durango"],
                                       [11, "Guanajuato"],
                                       [12, "Guerrero"],
                                       [13, "Hidalgo"],
                                       [14, "Jalisco"],
                                       [15, "Estado de México"],
                                       [16, "Michoacán de Ocampo"],
                                       [17, "Morelos"],
                                       [18, "Nayarit"],
                                       [19, "Nuevo León"],
                                       [20, "Oaxaca"],
                                       [21, "Puebla"],
                                       [22, "Querétaro"],
                                       [23, "Quintana Roo"],
                                       [24, "San Luis Potosí"],
                                       [25, "Sinaloa"],
                                       [26, "Sonora"],
                                       [27, "Tabasco"],
                                       [28, "Tamaulipas"],
                                       [29, "Tlaxcala"],
                                       [30, "Veracruz"],
                                       [31, "Yucatán"],
                                       [32, "Zacatecas"],
                                   ]
                                   )

    educacion = models.IntegerField(label="",
                               choices=[
                                   [1, "No asistió"],
                                   [2, "Primaria"],
                                   [3, "Secundaria "],
                                   [4, "Preparatoria"],
                                   [5, "Técnica"],
                                   [6, "Normal básica o de licenciatura"],
                                   [7, "Profesional (licenciatura o ingeniería)"],
                                   [8, "Postgrado (maestría o doctorado)"],
                               ],
                               blank=True
                               )
    empleo = models.IntegerField(label="",
                                   choices=[
                                       [1, "Empleado a tiempo completo"],
                                       [2, "Empleado a tiempo parcial"],
                                       [3, "Cuenta propia o emprendedor"],
                                       [4, "Desempleado y buscando trabajo"],
                                       [5, "Estudiante"],
                                       [6, "No estoy en la fuerza laboral(por ejemplo es padre o madre de tiempo completo)"],
                                   ]
                                   )
    ingreso_hogar = models.IntegerField(label="",
                                        choices=[
                                            [1, "$0 - $10,000"],
                                            [2, "$10,001 - $20,000"],
                                            [3, "$20,001 - $30,000"],
                                            [4, "$30,001 + "],
                                        ],
                                        blank=True
                                   )
    ### Preguntas sobre percepciones específicas
    percepcion_1 = models.IntegerField(label="",
                        min=0, max=10,
                        initial=0,
                        blank= False
                        )
    ingreso_pobre = models.PositiveIntegerField(label="$",
                                      )
    ingreso_rico = models.PositiveIntegerField(label="$",
                                      )

    personas = models.IntegerField(label="Personas pobres",
                        min=0, max=10,
                        initial=0,
                        blank= False
                        )
    personas2= models.IntegerField(label="Personas ricas",
                        min=0, max=10,
                        initial=0,
                        blank= False
                        )
    ### Percepción sobre la sociedad
    sociedad_nivel = models.IntegerField(label="",
                                 choices=[
                                     [1, "Sociedad A"],
                                     [2, "Sociedad B"],
                                     [3, "Sociedad C"],
                                     [4, "Sociedad D"],
                                     [5, "Sociedad E"],
                                     [6, "Sociedad F"],
                                 ]
                                 )
    sociedad_nivel2 = models.IntegerField(label="",
                                 choices=[
                                     [4, "Sociedad A"],
                                     [5, "Sociedad B"],
                                     [6, "Sociedad C"],
                                     [1, "Sociedad D"],
                                     [2, "Sociedad E"],
                                     [3, "Sociedad F"],
                                 ]
                                 )
    sociedad_nivel3 = models.IntegerField(label="",
                                 choices=[
                                     [1, "Sociedad A"],
                                     [3, "Sociedad B"],
                                     [5, "Sociedad C"],
                                     [2, "Sociedad D"],
                                     [4, "Sociedad E"],
                                     [6, "Sociedad F"],
                                 ]
                                 )
    sociedad_nivel4 = models.IntegerField(label="",
                                 choices=[
                                     [3, "Sociedad A"],
                                     [2, "Sociedad B"],
                                     [1, "Sociedad C"],
                                     [6, "Sociedad D"],
                                     [5, "Sociedad E"],
                                     [4, "Sociedad F"],
                                 ]
                                 )
    ### Mostrar gráficas interactivas para que elijan la sociedad ideal
    sociedad_ideal = models.IntegerField(
        label="",
        choices=[
            [1, "Sociedad A"],
            [2, "Sociedad B"],
            [3, "Sociedad C"],
            [4, "Sociedad D"],
            [5, "Sociedad E"],
            [6, "Sociedad F"],
        ]
        )
    sociedad_ideal2 = models.IntegerField(
        label="",
        choices=[
            [4, "Sociedad A"],
            [5, "Sociedad B"],
            [6, "Sociedad C"],
            [1, "Sociedad D"],
            [2, "Sociedad E"],
            [3, "Sociedad F"],
        ]
        )
    sociedad_ideal3 = models.IntegerField(
        label="",
        choices=[
            [6, "Sociedad A"],
            [5, "Sociedad B"],
            [4, "Sociedad C"],
            [3, "Sociedad D"],
            [2, "Sociedad E"],
            [1, "Sociedad F"],
        ]
        )
    sociedad_ideal4 = models.IntegerField(
        label="",
        choices=[
            [6, "Sociedad A"],
            [2, "Sociedad B"],
            [4, "Sociedad C"],
            [3, "Sociedad D"],
            [5, "Sociedad E"],
            [1, "Sociedad F"],
        ]
        )
    ### Preguntas sobre el gobierno finales
    gobierno_diferencias = models.BooleanField(label = "",
        choices=[[True,'Sí'],[False, 'No']]
                                )
    gobierno_apoyo = models.BooleanField(label = "",
        choices=[[True,'Sí'],[False, 'No']]
                                )
    ### ¿Cuánto cree que se DEBERIA pagar en impuestos? Grupos de tratamiento
    impuestos_deber_individuo = models.IntegerField(
        label="$",
        min=0, max=10,
        )
    impuestos_deber_ricos = models.IntegerField(
        label="$",
        min=0, max=10,
        initial=0,
        widget=widgets.SliderInput
        )
    impuestos_deber_pobres = models.IntegerField(
        label="$",
        min=0, max=10,
        initial=0,
        widget=widgets.SliderInput
        )
    impuestos_deber_med = models.IntegerField(
        label="$",
        min=0, max=10,
        initial=0,
        widget=widgets.SliderInput
    )
    ### ¿Cuánto cree que se DEBERIA pagar en impuestos? Grupo control
    impuestos_deber_individuo_prev = models.IntegerField(
        label="$",
        min=0, max=10,
        initial=0,
        widget=widgets.SliderInput
        )
    impuestos_deber_ricos_prev = models.IntegerField(
        label="$",
        min=0, max=10,
        initial=0,
        widget=widgets.SliderInput
        )
    impuestos_deber_pobres_prev = models.IntegerField(
        label="$",
        min=0, max=10,
        initial=0,
        widget=widgets.SliderInput
        )
    impuestos_deber_med_prev = models.IntegerField(
        label="$",
        min=0, max=10,
        initial=0,
        widget=widgets.SliderInput
    )
    ### ¿Cuánto cree que se paga en impuestos? Grupo control y tratamientos
    impuestos_cree_individuo_prev = models.IntegerField(
        label="$",
        min=0, max=10,
        )
    impuestos_cree_ricos_prev = models.IntegerField(
        label="$",
        min=0, max=10,
        initial=0,
        widget=widgets.SliderInput
        )
    impuestos_cree_pobres_prev = models.IntegerField(
        label="$",
        min=0, max=10,
        initial=0,
        widget=widgets.SliderInput
        )
    impuestos_cree_med_prev = models.IntegerField(
        label="$",
        min=0, max=10,
        initial=0,
        widget=widgets.SliderInput
        )

    ### Hacer que las personas toquen los sliders para las distintas páginas y tratamientos (mandatory sliders)
    checkslider = models.IntegerField(blank=True)
    checkslider2= models.IntegerField(blank=True)
    checkslidernew = models.IntegerField(blank=True)
    checkslidermed = models.IntegerField(blank=True)
    checkslider3 = models.IntegerField(blank=True)
    checkslider4 = models.IntegerField(blank=True)
    checkslider5 = models.IntegerField(blank=True)
    checkslider6 = models.IntegerField(blank=True)
    checkslider_prev = models.IntegerField(blank=True)
    checkslider2_prev = models.IntegerField(blank=True)
    checkslidernew_prev = models.IntegerField(blank=True)
    checkslidermed_prev = models.IntegerField(blank=True)
    checkslider_prev_cree = models.IntegerField(blank=True)
    checkslider2_prev_cree = models.IntegerField(blank=True)
    checkslidernew_prev_cree = models.IntegerField(blank=True)
    checkslidermed_prev_cree = models.IntegerField(blank=True)