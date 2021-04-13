from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from django.shortcuts import redirect


class Inicio(Page):
    form_model = "player"
    form_fields = ["participa", "prolific_id" ]
class SurveyQuestions(Page):
    form_model = "player"
    form_fields = ["edad", "sexo", "es_civil","nacimiento","educacion","empleo","ingreso_hogar"]
    def is_displayed(self):
        return self.player.participa == 1
class Percepciones(Page):
    form_model = "player"
    form_fields = ["percepcion_1", "ingreso_pobre", "ingreso_rico", "personas", "personas2", "checkslider3", "checkslider5","checkslider6",]
    def is_displayed(self):
        return self.player.participa == 1
    def checkslider3_error_message(self, value):
        if not value:
            return 'Por favor, recuerde tomar su decisión moviendo los sliders'
    def checkslider5_error_message(self, value):
        if not value:
            return 'Por favor, recuerde tomar su decisión moviendo los sliders'
    def checkslider6_error_message(self, value):
        if not value:
            return 'Por favor, recuerde tomar su decisión moviendo los sliders'

class Percepciones2(Page):
    form_model = "player"
    form_fields = ["sociedad_nivel"]
    def is_displayed(self):
        return self.player.percepciones_s == 2  and self.player.participa == 1
class Percepciones3(Page):
    form_model = "player"
    form_fields = ["sociedad_nivel2"]
    def is_displayed(self):
        return self.player.percepciones_s == 3 and self.player.participa == 1
class Percepciones4(Page):
    form_model = "player"
    form_fields = ["sociedad_nivel3"]
    def is_displayed(self):
        return self.player.percepciones_s == 4 and self.player.participa == 1
class Percepciones5(Page):
    form_model = "player"
    form_fields = ["sociedad_nivel4"]
    def is_displayed(self):
        return self.player.percepciones_s == 5 and self.player.participa == 1
class Ideales(Page):
    form_model = "player"
    form_fields = ["sociedad_ideal"]
    def is_displayed(self):
        return self.player.ideal_s == 1 and self.player.participa == 1
class Ideales2(Page):
    form_model = "player"
    form_fields = ["sociedad_ideal2"]
    def is_displayed(self):
        return self.player.ideal_s == 2 and self.player.participa == 1
class Ideales3(Page):
    form_model = "player"
    form_fields = ["sociedad_ideal3"]
    def is_displayed(self):
        return self.player.ideal_s == 3 and self.player.participa == 1
class Ideales4(Page):
    form_model = "player"
    form_fields = ["sociedad_ideal4"]
    def is_displayed(self):
        return self.player.ideal_s == 4 and self.player.participa == 1
class PT(Page):
    form_model = "player"
    form_fields = ["gobierno_apoyo", "gobierno_diferencias",]

    def is_displayed(self):
        return self.player.participa == 1

class SurveyFinal2(Page):
    timeout_seconds = 60
    def is_displayed(self):
        return self.player.participa == 0
class SurveyFinal3(Page):
    timeout_seconds = 180
    def is_displayed(self):
        return self.player.participa == 1
class T1(Page):
    form_model = 'player'
    form_fields = ['checkslider', 'checkslider2', 'checkslidernew', 'checkslidermed', 'impuestos_deber_individuo', 'impuestos_deber_ricos', 'impuestos_deber_pobres', 'impuestos_deber_med']
    def is_displayed(self):
        return self.player.tratamiento== 1 and self.player.participa == 1
    def checkslider_error_message(self, value):
        if not value:
            return 'Por favor, recuerde tomar su decisión moviendo los sliders'
    def checkslider2_error_message(self, value):
        if not value:
            return 'Por favor, recuerde tomar su decisión moviendo los sliders'
    def checkslidernew_error_message(self, value):
        if not value:
            return 'Por favor, recuerde tomar su decisión moviendo los sliders'
    def checkslidermed_error_message(self, value):
        if not value:
            return 'Por favor, recuerde tomar su decisión moviendo los sliders'
class T2(Page):
    form_model = 'player'
    form_fields = ['checkslider', 'checkslider2', 'checkslidernew', 'checkslidermed', 'impuestos_deber_individuo', 'impuestos_deber_ricos', 'impuestos_deber_pobres', 'impuestos_deber_med']
    def is_displayed(self):
        return self.player.tratamiento == 2 and self.player.participa == 1
    def checkslider_error_message(self, value):
        if not value:
            return 'Por favor, recuerde tomar su decisión moviendo los sliders'
    def checkslider2_error_message(self, value):
        if not value:
            return 'Por favor, recuerde tomar su decisión moviendo los sliders'
    def checkslidernew_error_message(self, value):
        if not value:
            return 'Por favor, recuerde tomar su decisión moviendo los sliders'
    def checkslidermed_error_message(self, value):
        if not value:
            return 'Por favor, recuerde tomar su decisión moviendo los sliders'
class T3(Page):
    form_model = 'player'
    form_fields = ['checkslider', 'checkslider2', 'checkslidernew', 'checkslidermed', 'impuestos_deber_individuo', 'impuestos_deber_ricos', 'impuestos_deber_pobres', 'impuestos_deber_med']
    def is_displayed(self):
        return self.player.tratamiento == 3 and self.player.participa == 1
    def checkslider_error_message(self, value):
        if not value:
            return 'Por favor, recuerde tomar su decisión moviendo los sliders'
    def checkslider2_error_message(self, value):
        if not value:
            return 'Por favor, recuerde tomar su decisión moviendo los sliders'
    def checkslidernew_error_message(self, value):
        if not value:
            return 'Por favor, recuerde tomar su decisión moviendo los sliders'
    def checkslidermed_error_message(self, value):
        if not value:
            return 'Por favor, recuerde tomar su decisión moviendo los sliders'

class Debe(Page):
    form_model = 'player'
    form_fields = ['checkslider_prev', 'checkslider2_prev', 'checkslidernew_prev', 'checkslidermed_prev','impuestos_deber_individuo_prev', 'impuestos_deber_ricos_prev', 'impuestos_deber_pobres_prev', 'impuestos_deber_med_prev',]
    def is_displayed(self):
        return self.player.tratamiento == 0 and self.player.participa == 1
    def checkslider_prev_error_message(self, value):
        if not value:
            return 'Por favor, recuerde tomar su decisión moviendo los sliders'
    def checkslider2_prev_error_message(self, value):
        if not value:
            return 'Por favor, recuerde tomar su decisión moviendo los sliders'
    def checkslidernew_prev_error_message(self, value):
        if not value:
            return 'Por favor, recuerde tomar su decisión moviendo los sliders'
    def checkslidermed_prev_error_message(self, value):
        if not value:
            return 'Por favor, recuerde tomar su decisión moviendo los sliders'
class Cree(Page):
    form_model = 'player'
    form_fields = ['checkslider_prev_cree', 'checkslider2_prev_cree', 'checkslidernew_prev_cree','checkslidermed_prev_cree','impuestos_cree_individuo_prev', 'impuestos_cree_ricos_prev', 'impuestos_cree_pobres_prev','impuestos_cree_med_prev']

    def is_displayed(self):
        return self.player.participa == 1
    def checkslider_prev_cree_error_message(self, value):
        if not value:
            return 'Por favor, recuerde tomar su decisión moviendo los sliders'
    def checkslider2_prev_cree_error_message(self, value):
        if not value:
            return 'Por favor, recuerde tomar su decisión moviendo los sliders'
    def checkslidernew_prev_cree_error_message(self, value):
        if not value:
            return 'Por favor, recuerde tomar su decisión moviendo los sliders'
    def checkslidermed_prev_cree_error_message(self, value):
        if not value:
            return 'Por favor, recuerde tomar su decisión moviendo los sliders'

page_sequence = [Inicio, SurveyFinal2, Percepciones,  Percepciones2, Percepciones3, Percepciones4, Percepciones5, Ideales, Ideales2, Ideales3, Ideales4, Cree, Debe, T1, T2, T3,  PT, SurveyQuestions, SurveyFinal3]
