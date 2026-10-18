from manim import *
import numpy as np

class IntroduccionEntropia(Scene):
    def construct(self):
        # 1. Título e introducción
        titulo = Text("La Flecha del Tiempo y la Entropía", font_size=36, weight=BOLD)
        titulo.to_edge(UP)
        self.play(Write(titulo))
        self.wait(0.5)

        # 2. Crear la caja (Contenedor)
        caja = Square(side_length=4.5, color=WHITE, stroke_width=3)
        caja.shift(DOWN * 0.3)
        label_caja = Text("Caja Cerrada", font_size=20).next_to(caja, UP, buff=0.2)
        
        self.play(Create(caja), Write(label_caja))

        # 3. Partículas agrupadas en la esquina inferior izquierda (Estado Ordenado / Baja Entropía)
        num_particulas = 40
        np.random.seed(42) # Semilla para reproducibilidad

        particulas = VGroup()
        # Definir la esquina (cuadrante restringido)
        esquina_x = [-1.8, -0.4]
        esquina_y = [-2.0, -0.6]

        for _ in range(num_particulas):
            p = Dot(radius=0.08, color=BLUE_B)
            # Posición inicial en la esquina
            x = np.random.uniform(esquina_x[0], esquina_x[1])
            y = np.random.uniform(esquina_y[0], esquina_y[1])
            p.move_to(caja.get_center() + np.array([x, y, 0]))
            particulas.add(p)

        # Texto del Estado Inicial
        texto_estado = Text("Estado Ordenado (Baja Entropía)", color=BLUE_A, font_size=24)
        texto_estado.next_to(caja, DOWN, buff=0.4)

        self.play(FadeIn(particulas, lag_ratio=0.02), Write(texto_estado))
        self.wait(1.5)

        # 4. Difusión: Las partículas se esparcen por toda la caja (Pasa el tiempo)
        
        # Generar nuevas posiciones para toda la caja
        animaciones_espardimiento = []
        for p in particulas:
            # Posición final dentro de todo el límite de la caja
            x_final = np.random.uniform(-2.0, 2.0)
            y_final = np.random.uniform(-2.0, 2.0)
            pos_final = caja.get_center() + np.array([x_final, y_final, 0])
            
            # Movimiento hacia la nueva posición cambiando a color rojo (calor/dispersión)
            animaciones_espardimiento.append(p.animate.move_to(pos_final).set_color(RED_B))

        # Transición del texto
        texto_desorden = Text("Estado Desordenado (Alta Entropía)", color=RED_A, font_size=24)
        texto_desorden.next_to(caja, DOWN, buff=0.4)

        # Tiempo transcurriendo
        reloj_texto = Text("Tiempo t →", font_size=20, color=YELLOW).next_to(caja, RIGHT, buff=0.5)

        self.play(
            Write(reloj_texto),
            Transform(texto_estado, texto_desorden),
            *animaciones_espardimiento,
            run_time=4.0,
            rate_func=linear
        )
        self.wait(1)

        # 5. Intentar volver atrás (Irreversibilidad)
        alerta = Text("¡Nunca regresa solo a la esquina!", color=ORANGE, font_size=22)
        alerta.next_to(caja, UP, buff=0.2)

        self.play(Transform(label_caja, alerta), Indicate(particulas, color=RED_A))
        self.wait(1.5)

        # 6. Conclusión y Definición Final
        self.play(
            FadeOut(caja),
            FadeOut(particulas),
            FadeOut(label_caja),
            FadeOut(texto_estado),
            FadeOut(reloj_texto)
        )

        concepto_entropia = VGroup(
            Text("Entropía", font_size=48, color=BLUE_C, weight=BOLD),
            Text("La medida de la tendencia natural del universo", font_size=22),
            Text("hacia el desorden y la dispersión de la energía.", font_size=22)
        ).arrange(DOWN, buff=0.3)

        self.play(Write(concepto_entropia))
        self.wait(2)