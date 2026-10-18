from manim import *
import numpy as np

class EntropiaMicroestados(Scene):
    def construct(self):
        # 1. Título principal
        titulo = Text("Entropía: Microestados y Probabilidad", font_size=32, weight=BOLD)
        titulo.to_edge(UP)
        self.play(Write(titulo))
        self.wait(0.5)

        # 2. Caja contenedora del sistema
        caja = Square(side_length=4.2, color=WHITE, stroke_width=2)
        caja.shift(LEFT * 2.5 + DOWN * 0.3)
        label_estado = Text("Estado Sólido (Hielo)", font_size=22, color=BLUE_C).next_to(caja, UP, buff=0.2)

        # Crear la red cristalina (Grid para el sólido)
        rows, cols = 4, 4
        grid_points = []
        for i in range(rows):
            for j in range(cols):
                x = -1.35 + j * 0.9
                y = -1.35 + i * 0.9
                grid_points.append(np.array([x, y, 0]))

        # Enlaces del sólido (líneas de red)
        lineas_red = VGroup()
        for i in range(rows):
            for j in range(cols):
                p_actual = caja.get_center() + grid_points[i * cols + j]
                if j < cols - 1:
                    p_derecha = caja.get_center() + grid_points[i * cols + (j + 1)]
                    lineas_red.add(Line(p_actual, p_derecha, stroke_width=1.5, color=BLUE_E))
                if i < rows - 1:
                    p_arriba = caja.get_center() + grid_points[(i + 1) * cols + j]
                    lineas_red.add(Line(p_actual, p_arriba, stroke_width=1.5, color=BLUE_E))

        # Partículas
        particulas = VGroup()
        for pt in grid_points:
            dot = Dot(point=caja.get_center() + pt, radius=0.12, color=BLUE_B)
            particulas.add(dot)

        # 3. Panel de Información a la Derecha
        panel_derecho = VGroup()
        
        titulo_panel = Text("Física Estadística", font_size=22, weight=BOLD, color=GRAY_A)
        
        label_w = Text("Configuraciones posibles (W):", font_size=18, color=WHITE)
        num_w = MathTex("W = 1", font_size=34, color=YELLOW)
        w_box = VGroup(label_w, num_w).arrange(DOWN, aligned_edge=LEFT, buff=0.15)

        desc_solido = Text(
            "• Átomos en posiciones fijas\n• Estructura ordenada\n• Mínima libertad de movimiento",
            font_size=16,
            line_spacing=1.3,
            color=LIGHT_GRAY
        )

        panel_derecho.add(titulo_panel, w_box, desc_solido)
        panel_derecho.arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        panel_derecho.shift(RIGHT * 2.7 + DOWN * 0.3)

        self.play(
            Create(caja),
            Write(label_estado),
            Create(lineas_red),
            FadeIn(particulas, lag_ratio=0.05),
            FadeIn(panel_derecho)
        )
        self.wait(1)

        # Micro-vibraciones en el estado sólido
        vibraciones = []
        for p in particulas:
            pos_orig = p.get_center()
            vibraciones.append(
                p.animate(run_time=0.4, rate_func=there_and_back)
                .shift(np.random.uniform(-0.08, 0.08, 3))
            )
        self.play(*vibraciones)
        self.wait(1)

        # 4. Transición al Estado Líquido (Fusión)
        label_liquido = Text("Estado Líquido (Agua)", font_size=22, color=TEAL_B).next_to(caja, UP, buff=0.2)
        
        desc_liquido = Text(
            "• Libertad de desplazamiento\n• Múltiples trayectorias posibles\n• Innumerables acomodos",
            font_size=16,
            line_spacing=1.3,
            color=LIGHT_GRAY
        )

        # Romper los enlaces y cambiar color de partículas
        self.play(
            Uncreate(lineas_red),
            Transform(label_estado, label_liquido),
            particulas.animate.set_color(TEAL_A),
            run_time=1.5
        )

        # Múltiples trayectorias/configuraciones posibles (Líneas multicolores)
        np.random.seed(101)
        trayectorias = VGroup()
        colores_trayectorias = [TEAL_C, GREEN_B, PURPLE_B, YELLOW_D, ORANGE]

        for p in particulas:
            p_inicio = p.get_center()
            # Generar un camino curvo dentro de la caja
            p_intermedio = p_inicio + np.random.uniform(-0.8, 0.8, 3)
            p_final = caja.get_center() + np.random.uniform(-1.5, 1.5, 3)
            
            camino = CubicBezier(
                p_inicio,
                p_inicio + np.random.uniform(-0.4, 0.4, 3),
                p_intermedio,
                p_final
            )
            camino.set_stroke(
                color=np.random.choice(colores_trayectorias),
                width=1.5,
                opacity=0.6
            )
            trayectorias.add(camino)

        # Contador de configuraciones aumentando rápidamente
        num_w_liquido = MathTex(r"W \approx 10^{23}", font_size=34, color=YELLOW)
        num_w_liquido.move_to(num_w.get_center(), aligned_edge=LEFT)

        self.play(
            Create(trayectorias, lag_ratio=0.02),
            Transform(num_w, num_w_liquido),
            Transform(desc_solido, desc_liquido),
            run_time=2.5
        )

        # Movimiento líquido de partículas a lo largo de sus posiciones
        movimiento_liquido = []
        for i, p in enumerate(particulas):
            nueva_pos = trayectorias[i].get_end()
            movimiento_liquido.append(p.animate.move_to(nueva_pos))

        self.play(*movimiento_liquido, run_time=2.0)
        self.wait(1)

        # 5. Conclusión: Fórmula de Boltzmann
        formula_boltzmann = MathTex(
            "S", "=", "k_B", r"\cdot \ln(", "W", ")",
            font_size=36
        )
        formula_boltzmann.set_color_by_tex("S", RED_B)
        formula_boltzmann.set_color_by_tex("W", YELLOW)
        formula_boltzmann.next_to(desc_liquido, DOWN, buff=0.5).align_to(desc_liquido, LEFT)

        explicacion_final = Text(
            "Mayor N° de formas posibles (W)\n= Mayor Entropía (S)",
            font_size=15,
            color=YELLOW_A,
            line_spacing=1.2
        ).next_to(formula_boltzmann, DOWN, buff=0.3).align_to(formula_boltzmann, LEFT)

        self.play(
            Write(formula_boltzmann),
            FadeIn(explicacion_final)
        )
        self.wait(2.5)
`