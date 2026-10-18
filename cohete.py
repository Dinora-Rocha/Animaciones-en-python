from manim import *
import random

class DespegueCohete(Scene):
    def construct(self):
        # Fondo oscuro espacial
        self.camera.background_color = "#0B0C10"

        # 1. DISEÑO DEL COHETE
        cuerpo = Rectangle(width=0.8, height=2.5, color=LIGHT_GREY, fill_opacity=1)
        punta = Cone(base_radius=0.4, height=0.9, direction=UP, color=RED, fill_opacity=1)
        punta.next_to(cuerpo, UP, buff=0)

        ventana_borde = Circle(radius=0.25, color=DARK_GREY, fill_opacity=1)
        ventana_cristal = Circle(radius=0.2, color=BLUE_A, fill_opacity=0.8)
        ventana = VGroup(ventana_borde, ventana_cristal).move_to(cuerpo.get_center() + UP * 0.4)

        # Alerones laterales
        aleron_izq = Polygon([-0.4, -1.25, 0], [-0.8, -1.6, 0], [-0.4, -0.5, 0], color=RED, fill_opacity=1)
        aleron_der = Polygon([0.4, -1.25, 0], [0.8, -1.6, 0], [0.4, -0.5, 0], color=RED, fill_opacity=1)

        # Tobera/Propulsor (Definida con Polygon para evitar errores de compatibilidad)
        tobera = Polygon(
            [-0.25, 0, 0],
            [0.25, 0, 0],
            [0.35, -0.3, 0],
            [-0.35, -0.3, 0],
            color=DARK_GREY,
            fill_opacity=1
        )
        tobera.next_to(cuerpo, DOWN, buff=0)

        # Agrupar todo el cohete
        cohete = VGroup(cuerpo, punta, ventana, aleron_izq, aleron_der, tobera)
        cohete.move_to(DOWN * 2)

        # 2. FUEGO Y PROPULSIÓN
        fuego_exterior = Triangle(color=ORANGE, fill_opacity=0.9).scale(0.5).rotate(PI)
        fuego_exterior.next_to(tobera, DOWN, buff=0)
        
        fuego_interior = Triangle(color=YELLOW, fill_opacity=1).scale(0.3).rotate(PI)
        fuego_interior.next_to(tobera, DOWN, buff=0)

        fuego = VGroup(fuego_exterior, fuego_interior)

        # 3. HUMO DE DESPEGUE (Partículas)
        particulas_humo = VGroup()
        for _ in range(18):
            radio = random.uniform(0.15, 0.35)
            nube = Circle(radius=radio, color=GRAY_C, fill_opacity=0.4, stroke_width=0)
            nube.move_to(DOWN * 3.3 + RIGHT * random.uniform(-1.5, 1.5))
            particulas_humo.add(nube)

        # 4. ANIMACIÓN DEL DESPEGUE
        
        # Ensamblaje
        self.play(DrawBorderThenFill(cohete), run_time=1.5)
        self.wait(0.5)

        # Ignición: Fuego y humo
        self.play(
            FadeIn(fuego, scale=0.2),
            LaggedStart(*[GrowFromCenter(p) for p in particulas_humo], lag_ratio=0.05),
            run_time=0.8
        )

        # Vibración previa al lanzamiento
        self.play(
            cohete.animate.shift(RIGHT * 0.05),
            fuego.animate.shift(RIGHT * 0.05),
            rate_func=wiggle,
            run_time=0.6
        )

        # Despegue acelerado
        self.play(
            cohete.animate.shift(UP * 9),
            fuego.animate.shift(UP * 9).scale(1.4),
            particulas_humo.animate.scale(2.5).set_opacity(0),
            run_time=3.5,
            rate_func=rate_functions.ease_in_cubic
        )
        self.wait(1)