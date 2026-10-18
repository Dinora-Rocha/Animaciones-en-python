from manim import *
import numpy as np

class PatronSecreto(Scene):
    def construct(self):
        # Configuración de fondo oscuro
        self.camera.background_color = "#0D0E15"

        # -------------------------------------------------------------
        # ESCENA 1: PÉTALOS Y CONTEO
        # -------------------------------------------------------------
        titulo = Text("El Patrón Oculto en la Naturaleza", font_size=36, color=WHITE).to_edge(UP)
        self.play(Write(titulo))
        self.wait(0.5)

        # Crear flor de 5 pétalos
        centro_flor = Circle(radius=0.4, color=YELLOW, fill_opacity=1)
        petalos = VGroup()
        num_petalos = 5
        
        for i in range(num_petalos):
            p = Ellipse(width=0.6, height=1.8, color=PINK, fill_opacity=0.7)
            p.shift(UP * 0.9)
            p.rotate(i * (2 * PI / num_petalos), about_point=ORIGIN)
            petalos.add(p)

        flor = VGroup(petalos, centro_flor).scale(1.1)

        self.play(GrowFromCenter(centro_flor), LaggedStart(*[GrowFromCenter(p) for p in petalos], lag_ratio=0.1))
        
        # Mostrar el número de pétalos
        num_text = MathTex("5", font_size=72, color=YELLOW).next_to(flor, RIGHT, buff=1.5)
        etiqueta_petalos = Text("pétalos", font_size=24, color=WHITE).next_to(num_text, DOWN)
        
        self.play(Write(num_text), FadeIn(etiqueta_petalos))
        self.wait(1.5)

        # -------------------------------------------------------------
        # TRANSICIÓN A ESCENA 2: ESPIRALES DEL GIRASOL (Ángulo Dorado)
        # -------------------------------------------------------------
        self.play(
            Unwrite(etiqueta_petalos),
            Unwrite(num_text),
            FadeOut(petalos),
            centro_flor.animate.scale(0.1).move_to(ORIGIN)
        )

        # Espiral de Vogel (Girasol) usando el Ángulo Dorado (~137.5 grados = 2.39996 rad)
        angulo_dorado = 2.3999632297286533
        semillas = VGroup()
        num_semillas = 120

        for i in range(num_semillas):
            r = 0.25 * np.sqrt(i)
            theta = i * angulo_dorado
            pos = np.array([r * np.cos(theta), r * np.sin(theta), 0])
            
            # Alternar colores para resaltar la formación de espirales
            color_semilla = GOLD if i % 2 == 0 else ORANGE
            semilla = Dot(point=pos, radius=0.06, color=color_semilla)
            semillas.add(semilla)

        # Animación de las semillas apareciendo en espiral
        self.play(
            LaggedStart(*[Create(s) for s in semillas], lag_ratio=0.02),
            run_time=3
        )
        self.wait(1.5)

        # -------------------------------------------------------------
        # TRANSICIÓN A ESCENA 3: REPRODUCCIÓN DE CONEJOS
        # -------------------------------------------------------------
        # Desvanecer semillas
        self.play(
            FadeOut(semillas),
            FadeOut(centro_flor)
        )

        # Crear Siluetas / Diseños de Conejitos con formas simples
        def crear_conejito():
            cuerpo = Ellipse(width=0.9, height=1.1, color=LIGHT_GREY, fill_opacity=1)
            cabeza = Circle(radius=0.35, color=LIGHT_GREY, fill_opacity=1).next_to(cuerpo, UP*0.8, buff=-0.15)
            oreja_izq = Ellipse(width=0.18, height=0.7, color=LIGHT_GREY, fill_opacity=1).rotate(0.2).next_to(cabeza, UP*0.8 + LEFT*0.2, buff=-0.1)
            oreja_der = Ellipse(width=0.18, height=0.7, color=LIGHT_GREY, fill_opacity=1).rotate(-0.2).next_to(cabeza, UP*0.8 + RIGHT*0.2, buff=-0.1)
            ojo = Dot(color=BLACK, radius=0.04).move_to(cabeza.get_center() + RIGHT*0.1 + UP*0.05)
            
            # Detalle oreja interior
            oreja_in_izq = Ellipse(width=0.08, height=0.5, color=PINK, fill_opacity=0.8).move_to(oreja_izq)
            oreja_in_der = Ellipse(width=0.08, height=0.5, color=PINK, fill_opacity=0.8).move_to(oreja_der)
            
            return VGroup(cuerpo, cabeza, oreja_izq, oreja_der, oreja_in_izq, oreja_in_der, ojo).scale(0.8)

        conejo_izq = crear_conejito().move_to(LEFT * 2)
        conejo_der = crear_conejito().move_to(RIGHT * 2)
        conejo_der.flip(axis=UP) # Reflejar para que se miren de frente

        # Crear un Corazón en el centro
        corazon = ParametricFunction(
            lambda t: np.array([
                0.25 * (16 * np.sin(t)**3),
                0.25 * (13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)),
                0
            ]),
            t_range=[0, TAU],
            color=RED,
            fill_opacity=1
        ).scale(0.2).move_to(UP * 0.5)

        # Animación de los conejitos entrando y el corazón latiendo/apareciendo
        self.play(
            GrowFromCenter(conejo_izq),
            GrowFromCenter(conejo_der),
            run_time=1.5
        )
        
        self.play(
            DrawBorderThenFill(corazon),
            run_time=1
        )

        # Latido del corazón
        self.play(
            corazon.animate.scale(1.3),
            rate_func=there_and_back,
            run_time=0.6
        )
        self.play(
            corazon.animate.scale(1.3),
            rate_func=there_and_back,
            run_time=0.6
        )

        # Secuencia matemática implícita en pantalla (1, 1, 2, 3, 5, 8...)
        secuencia = MathTex("1", ",", "1", ",", "2", ",", "3", ",", "5", ",", "8", ",", "13", r", \dots", font_size=42, color=GOLD)
        secuencia.next_to(VGroup(conejo_izq, conejo_der), DOWN, buff=1.0)

        self.play(Write(secuencia), run_time=2.5)
        self.wait(2)