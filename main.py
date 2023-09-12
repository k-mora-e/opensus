#import random
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.clock import Clock
from kivy.core.window import Window
#from kivy.config import Config
from kivy.uix.widget import Widget
from kivy.graphics import Line, Color


class so(App):
    def build(self):
        self.altura = 0.05
        self.ball_x = 0.5
        self.ball_y = 0.5
        self.maxpoint = 5

        self.contador_2, self.contador_1 = 0, 0



        self.player_2_x, self.player_2_y = 0, 0

        self.layout = FloatLayout()
        Window.size = (700, 300)
        self.fondo = Image(source="img/fondo.jpg", size_hint=(1, 1), allow_stretch=True, keep_ratio=False)
        self.layout.add_widget(self.fondo)

        self.play = Button(text="Play",  background_color=(0.85, 0.56, 0.57, 1))
        self.play.size_hint = (0.1, 0.1)
        self.play.bind(on_press=self.playbutton)
        self.play.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
        self.layout.add_widget(self.play)

        self.up = Button(background_normal="img/up_key.png",
                         background_down="img/up_key_press.png")
        self.up.pos_hint = {'center_x': 0.85, 'center_y': 0.15}

        self.up.bind(on_press=self.start_up_button)
        self.up.bind(on_release=self.stop_up_button)
        self.up.size_hint = (0.2, 0.4)


        self.down = Button(background_normal="img/down_key.png",
                           background_down="img/down_key_press.png")
        self.down.bind(on_press=self.start_down_button)
        self.down.bind(on_release=self.stop_down_button)
        self.down.pos_hint = {'center_x': 0.7, 'center_y': 0.15}
        self.down.size_hint = (0.2, 0.4)

        self.player_1 = Image(source="img/green_sus.png")
        self.hitbox_1 = Widget(size_hint=(0.05, 0.2))
        self.player_1.pos_hint = {'center_x': self.altura, 'center_y': 0.1}
        self.hitbox_1.pos_hint = {'center_x': self.altura, 'center_y': 0.1}

        self.player_2 = Image(source="img/red_sus.png")
        self.hitbox_2 = Widget(size_hint=(0.05, 0.2))
        self.player_2.pos_hint = {'center_x': 0.95, 'center_y': 0.3}
        self.hitbox_2.pos_hint = {'center_x': 0.95, 'ceter_y': 0.3}

        self.ball = Image(source="img/toilet.png")
        self.ballbox = Widget(size_hint=(0.02, 0.02))
        self.ballbox.pos_hint = {'center_x': self.ball_x, 'center_y': self.ball_y}


        self.contador_1_label = Label(text=str(self.contador_1), color=(1, 1, 1, 1))
        self.contador_1_label.pos_hint = {'center_x': 0.4, 'center_y': 0.9}
        self.contador_2_label = Label(text=str(self.contador_2), color=(1, 1, 1, 1))
        self.contador_2_label.pos_hint = {'center_x': 0.6, 'center_y': 0.9}


        self.ball_speed = [0.8, 0.8]  # Velocidad de movimiento de la bola
        self.up_button_pressed = False  # Inicializar la variable
        self.down_button_pressed = False  # Inicializar la variable

        self.retry = Button(text="Retry", background_color=(0.85, 0.56, 0.57, 1))
        self.retry.bind(on_press=self.retryButton)
        self.retry.pos_hint = {'center_x': 0.5, 'center_y': 0.1}
        self.retry.size_hint = (0.1, 0.1)

        self.derrotaimg = Image(source="img/derrota.jpeg")
        self.DERROTA = Label(text="DERROTA", color=(1, 0, 0, 1))
        self.DERROTA.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
        self.DERROTA.size_hint = (0.4, 0.4)
        self.DERROTA.font_size = 32

        self.victoriaimg = Image(source="img/victoria.jpeg")
        self.VICTORIA = Label(text="VICTORIA", color=(0, 1, 0, 1))
        self.VICTORIA.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
        self.VICTORIA.size_hint = (0.4, 0.4)
        self.VICTORIA.font_size = 32

        self.puntos1 = Button(text="10", background_color=(0.85, 0.56, 0.57, 1))
        self.puntos1.bind(on_press=self.diespoint)
        self.puntos1.pos_hint = {'center_x': 0.1, 'center_y': 0.55}
        self.puntos1.size_hint = (0.1, 0.1)
        self.layout.add_widget(self.puntos1)

        self.puntos2 = Button(text="15", background_color=(0.85, 0.56, 0.57, 1))
        self.puntos2.bind(on_press=self.quincepuntos)
        self.puntos2.pos_hint = {'center_x': 0.1, 'center_y': 0.4}
        self.puntos2.size_hint = (0.1, 0.1)
        self.layout.add_widget(self.puntos2)

        self.puntos3 = Button(text="20", background_color=(0.85, 0.56, 0.57, 1))
        self.puntos3.bind(on_press=self.veinte)
        self.puntos3.pos_hint = {'center_x': 0.1, 'center_y': 0.25}
        self.puntos3.size_hint = (0.1, 0.1)
        self.layout.add_widget(self.puntos3)

        self.puntos4 = Button(text="5", background_color=(0.85, 0.56, 0.57, 1))
        self.puntos4.bind(on_press=self.cinco)
        self.puntos4.pos_hint = {'center_x': 0.1, 'center_y': 0.7}
        self.puntos4.size_hint = (0.1, 0.1)
        self.layout.add_widget(self.puntos4)

        return self.layout


    def diespoint(self, instance):
        self.maxpoint = 10
    def quincepuntos(self, instance):
        self.maxpoint = 15
    def veinte(self, instance):
        self.maxpoint = 20
    def cinco(self, instance):
        self.maxpoint = 5
    def retryButton(self, instance):
        self.layout.clear_widgets()
        self.layout.add_widget(self.fondo)
        self.layout.add_widget(self.play)
        self.layout.add_widget(self.puntos1)
        self.layout.add_widget(self.puntos2)
        self.layout.add_widget(self.puntos3)
        self.layout.add_widget(self.puntos4)
        self.contador_2, self.contador_1 = 0, 0
        self.contador_1_label.text = "0"
        self.contador_2_label.text = "0"
        self.ball_x, self.ball_y = 0.5, 0.5
        Clock.schedule_once(self.update, 0.1)
        Clock.unschedule(self.update)
        Clock.unschedule(self.move_ball)
    def playbutton(self, instance):
        self.layout.remove_widget(self.play)
        self.layout.remove_widget(self.puntos1)
        self.layout.remove_widget(self.puntos2)
        self.layout.remove_widget(self.puntos3)
        self.layout.remove_widget(self.puntos4)

        self.layout.add_widget(self.up)
        self.layout.add_widget(self.down)
        self.layout.add_widget(self.player_1)
        self.layout.add_widget(self.player_2)
        self.layout.add_widget(self.hitbox_1)
        self.layout.add_widget(self.hitbox_2)
        self.layout.add_widget(self.ballbox)
        self.layout.add_widget(self.contador_1_label)
        self.layout.add_widget(self.contador_2_label)

        with self.layout.canvas:
            Color(1, 0, 0)
            Line(points=[self.layout.width / 2, self.layout.height, self.layout.width / 2, 0], width=2)
        self.layout.add_widget(self.ball)

        Clock.schedule_interval(self.update, 1.0 / 180.0)
        Clock.schedule_interval(self.move_ball, 1.0 / 120.0)  # Agregar el movimiento de la bola

    def start_up_button(self, instance):
        self.up_button_pressed = True

    def stop_up_button(self, instance):
        self.up_button_pressed = False

    def start_down_button(self, instance):
        self.down_button_pressed = True

    def stop_down_button(self, instance):
        self.down_button_pressed = False

    def update(self, dt):
        ball_center_y = self.ball_y
        player_2_center_y = self.player_2_y

        # Mover el jugador 2 automáticamente hacia la posición de la bola en el eje vertical
        if ball_center_y > player_2_center_y and self.ball_x >= 0.5:
            player_2_center_y += 0.6 * dt
        elif ball_center_y < player_2_center_y and self.ball_x >= 0.5:
            player_2_center_y -= 0.6 * dt

        # Limitar las posiciones del jugador 2 dentro de la pantalla
        player_2_center_y = max(0.1, min(0.9, player_2_center_y))

        # Actualizar la posición del jugador 2
        self.player_2_y = player_2_center_y
        self.player_2.pos_hint = {'center_x': 0.95, 'center_y': self.player_2_y}
        self.hitbox_2.pos_hint = {'center_x': 0.95, 'center_y': self.player_2_y}


        # Mover el jugador 1
        if self.up_button_pressed:
            self.altura += 0.6 * dt
            if self.altura > 0.9:
                self.altura = 0.9
            self.player_1.pos_hint = {'center_x': 0.05, 'center_y': self.altura}
            self.hitbox_1.pos_hint = {'center_x': 0.05, 'center_y': self.altura}

        if self.down_button_pressed:
            self.altura -= 0.6 * dt
            if self.altura < 0.1:
                self.altura = 0.1
            self.player_1.pos_hint = {'center_x': 0.05, 'center_y': self.altura}
            self.hitbox_1.pos_hint = {'center_x': 0.05, 'center_y': self.altura}

    def move_ball(self, dt):
        # Actualizar la posición de la bola
        self.ball_x += self.ball_speed[0] * dt/2
        self.ball_y += self.ball_speed[1] * dt

        # Rebotar la bola en los límites de la pantalla
        if self.ball_x < 0:
            self.ball_speed[0] *= -1
            self.ball_x = 0.5
            self.contador_2 += 1
            self.contador_2_label.text = str(self.contador_2)
            if self.contador_2 == self.maxpoint:
                self.layout.clear_widgets()
                self.layout.add_widget(self.derrotaimg)
                self.layout.add_widget(self.DERROTA)
                Clock.unschedule(self.update)
                Clock.unschedule(self.move_ball)
                self.layout.add_widget(self.retry)



        if self.ball_x > 1:
            self.ball_speed[0] *= -1
            self.ball_x = 0.5
            self.contador_1 += 1
            self.contador_1_label.text = str(self.contador_1)
            if self.contador_1 == self.maxpoint:
                self.layout.clear_widgets()
                self.layout.add_widget(self.victoriaimg)
                self.layout.add_widget(self.VICTORIA)
                Clock.unschedule(self.update)
                Clock.unschedule(self.move_ball)
                self.layout.add_widget(self.retry)

        if self.ball_y < 0 or self.ball_y > 1:
            self.ball_speed[1] *= -1

        # Rebotar la bola en las hit boxes
        if self.hitbox_1.collide_widget(self.ballbox):
            self.ball_x += 0.01
            self.ball_speed[0] *= -1
        if self.hitbox_2.collide_widget(self.ballbox):
            self.ball_x -= 0.01
            self.ball_speed[0] *= -1


        # Actualizar la posición de la bola en la pantalla
        self.ballbox.pos_hint = {'center_x': self.ball_x, 'center_y': self.ball_y}
        self.ball.pos_hint = {'center_x': self.ball_x, 'center_y': self.ball_y}

if __name__ == "__main__":
    so().run()
