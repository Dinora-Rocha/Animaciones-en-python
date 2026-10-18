from manim import *
import numpy as np

# Semilla fija para que el "huevo roto" se vea siempre igual
# (sin esto, cada render generaría una salpicadura distinta)
np.random.seed(7)


class FlechaDelTiempo(Scene):

    def construct(self):

        # ============================================================
        # CONFIGURACIÓN
        # ============================================================

        self.camera.background_color = "#05070A"

        # ============================================================
        # TÍTULO
        # ============================================================

        titulo = Text(
            "La Flecha del Tiempo",
            font_size=40
        )

        titulo.to_edge(UP, buff=0.35)

        self.play(
            Write(titulo),
            run_time=1.2
        )

        # ============================================================
        # INTRODUCCIÓN
        # ============================================================

        texto = VGroup(
            Text(
                "Las leyes fundamentales de la física",
                font_size=24
            ),
            Text(
                "pueden funcionar hacia adelante y hacia atrás.",
                font_size=24
            ),
            Text(
                "Pero la entropía introduce una dirección.",
                font_size=24
            )
        )

        texto.arrange(
            DOWN,
            buff=0.18
        )

        texto.next_to(
            titulo,
            DOWN,
            buff=0.45
        )

        self.play(
            FadeIn(texto, shift=DOWN),
            run_time=1.2
        )

        self.wait(2)

        self.play(
            FadeOut(texto),
            run_time=0.7
        )

        # ============================================================
        # ESCENA 1: PASADO → FUTURO
        # ============================================================

        etiqueta_pasado = Text(
            "PASADO",
            font_size=25
        )

        etiqueta_futuro = Text(
            "FUTURO",
            font_size=25
        )

        etiqueta_pasado.move_to(
            LEFT * 4.3 + DOWN * 0.2
        )

        etiqueta_futuro.move_to(
            RIGHT * 4.3 + DOWN * 0.2
        )

        # Flecha temporal (sustituye a la Line que no se usaba)
        flecha = Arrow(
            LEFT * 3.5,
            RIGHT * 3.5,
            buff=0,
            stroke_width=5
        )

        flecha.move_to(
            DOWN * 0.8
        )

        self.play(
            FadeIn(etiqueta_pasado),
            FadeIn(etiqueta_futuro),
            Create(flecha),
            run_time=1
        )

        # ============================================================
        # HUEVO ENTERO
        # ============================================================

        huevo = Ellipse(
            width=1.25,
            height=1.7
        )

        huevo.set_stroke(
            WHITE,
            width=3
        )

        huevo.set_fill(
            "#F2E9D8",
            opacity=1
        )

        huevo.move_to(
            LEFT * 3.2 + UP * 0.8
        )

        # Yema
        yema = Circle(
            radius=0.25
        )

        yema.set_fill(
            "#E8B94A",
            opacity=1
        )

        yema.set_stroke(
            width=0
        )

        yema.move_to(
            huevo.get_center()
        )

        huevo_completo = VGroup(
            huevo,
            yema
        )

        # ============================================================
        # HUEVO ROTO
        # ============================================================
        # La yema va primero y se dibuja ABAJO (z_index bajo);
        # las gotas de clara se generan evitando el centro exacto de
        # la yema, para que no se amontonen todas en el mismo punto
        # ni la tapen por completo.

        centro_charco = np.array([2.6, 0.7, 0])
        centro_yema_rota = np.array([2.9, -0.1, 0])

        yema_rota = Circle(
            radius=0.35
        )

        yema_rota.set_fill(
            "#E8B94A",
            opacity=1
        )

        yema_rota.set_stroke(
            width=0
        )

        yema_rota.move_to(centro_yema_rota)
        yema_rota.set_z_index(2)

        charcos = VGroup()
        radio_exclusion = 0.55  # no generar gotas pegadas a la yema

        for _ in range(9):

            angulo = np.random.uniform(0, 2 * np.pi)
            distancia = np.random.uniform(radio_exclusion, 1.25)

            x = centro_charco[0] + np.cos(angulo) * distancia
            y = centro_charco[1] + np.sin(angulo) * distancia * 0.55

            gota = Dot(
                point=np.array([x, y, 0]),
                radius=np.random.uniform(0.06, 0.16)
            )

            gota.set_fill(
                "#F2E9D8",
                opacity=1
            )

            gota.set_z_index(1)

            charcos.add(gota)

        # ============================================================
        # TRANSICIÓN DEL HUEVO
        # ============================================================

        self.play(
            FadeIn(huevo_completo),
            run_time=1
        )

        self.wait(1)

        self.play(
            FadeOut(huevo_completo),
            FadeIn(charcos),
            FadeIn(yema_rota),
            run_time=1.5
        )

        # ============================================================
        # TEXTO EXPLICATIVO
        # ============================================================

        huevo_texto = Text(
            "Un huevo puede romperse...",
            font_size=22
        )

        huevo_texto.to_edge(
            DOWN,
            buff=0.7
        )

        self.play(
            FadeIn(huevo_texto),
            run_time=0.8
        )

        self.wait(1.5)

        self.play(
            FadeOut(huevo_texto),
            FadeOut(charcos),
            FadeOut(yema_rota),
            FadeOut(etiqueta_pasado),
            FadeOut(etiqueta_futuro),
            FadeOut(flecha),
            run_time=0.8
        )

        # ============================================================
        # ESCENA 2: EL HUEVO NO SE RECONSTRUYE
        # ============================================================

        texto_huevo = Text(
            "Pero nunca se reconstruye espontáneamente.",
            font_size=25
        )

        texto_huevo.next_to(
            titulo,
            DOWN,
            buff=0.55
        )

        self.play(
            FadeIn(texto_huevo),
            run_time=0.8
        )

        # Partículas representando fragmentos
        fragmentos = VGroup()

        posiciones_iniciales = [
            [-2.5, 0.4, 0],
            [-1.5, -0.2, 0],
            [-0.5, 0.7, 0],
            [0.5, -0.5, 0],
            [1.5, 0.3, 0],
            [2.4, -0.1, 0],
        ]

        for pos in posiciones_iniciales:

            fragmento = Polygon(
                [-0.18, -0.15, 0],
                [0.2, -0.1, 0],
                [0.08, 0.18, 0]
            )

            fragmento.set_fill(
                WHITE,
                opacity=1
            )

            fragmento.set_stroke(
                width=1
            )

            fragmento.move_to(
                np.array(pos)
            )

            fragmentos.add(fragmento)

        self.play(
            FadeIn(fragmentos),
            run_time=0.8
        )

        # Intento visual de "volver atrás": los fragmentos SÍ pueden
        # reorganizarse en una figura ordenada (un cuadrado), porque
        # el desorden no impide que exista orden en general. Pero esa
        # figura ordenada nunca es el huevo original: ese es el punto.
        # Un cuadrado dividido en 3 franjas verticales, cada una
        # partida por su diagonal, da exactamente 6 triángulos que
        # encajan sin huecos ni traslapes.

        lado_cuadrado = 1.6
        centro_cuadrado = np.array([0, 0.1, 0])

        y_abajo = centro_cuadrado[1] - lado_cuadrado / 2
        y_arriba = centro_cuadrado[1] + lado_cuadrado / 2

        ancho_franja = lado_cuadrado / 3
        x_inicio = centro_cuadrado[0] - lado_cuadrado / 2

        triangulos_objetivo = []

        for i in range(3):

            x_izq = x_inicio + i * ancho_franja
            x_der = x_izq + ancho_franja

            triangulo_a = Polygon(
                [x_izq, y_abajo, 0],
                [x_der, y_abajo, 0],
                [x_izq, y_arriba, 0],
            )

            triangulo_b = Polygon(
                [x_der, y_abajo, 0],
                [x_der, y_arriba, 0],
                [x_izq, y_arriba, 0],
            )

            for t in (triangulo_a, triangulo_b):
                t.set_fill(WHITE, opacity=1)
                t.set_stroke("#AAAAAA", width=1)

            triangulos_objetivo.append(triangulo_a)
            triangulos_objetivo.append(triangulo_b)

        self.play(
            *[
                Transform(fragmentos[i], triangulos_objetivo[i])
                for i in range(len(fragmentos))
            ],
            run_time=2
        )

        self.play(
            Indicate(
                fragmentos,
                scale_factor=1.04,
                color=WHITE
            ),
            run_time=1
        )

        imposible = Text(
            "Formaron un cuadrado... pero nunca volverán a ser el huevo.",
            font_size=21
        )

        imposible.to_edge(
            DOWN,
            buff=0.7
        )

        self.play(
            FadeIn(imposible),
            run_time=0.8
        )

        self.wait(2)

        self.play(
            FadeOut(texto_huevo),
            FadeOut(fragmentos),
            FadeOut(imposible),
            run_time=0.8
        )

        # ============================================================
        # ESCENA 3: ENVEJECIMIENTO
        # ============================================================

        texto_edad = Text(
            "El tiempo también deja una huella en nosotros",
            font_size=25
        )

        texto_edad.next_to(
            titulo,
            DOWN,
            buff=0.55
        )

        self.play(
            FadeIn(texto_edad),
            run_time=0.8
        )

        # --- Persona joven ---
        cabeza_joven = Circle(radius=0.48)
        cabeza_joven.set_fill("#D9A066", opacity=1)
        cabeza_joven.set_stroke(width=2)

        # Ojos simples para que se lea claramente como un rostro
        ojo_izq_joven = Dot(radius=0.05, color=BLACK)
        ojo_der_joven = Dot(radius=0.05, color=BLACK)

        cuerpo_joven = RoundedRectangle(
            width=1.1,
            height=1.8,
            corner_radius=0.2
        )

        cuerpo_joven.set_fill("#4A78A8", opacity=1)
        cuerpo_joven.set_stroke(width=2)

        cabeza_joven.move_to(LEFT * 2.4 + DOWN * 0.25)
        cuerpo_joven.move_to(LEFT * 2.4 + DOWN * 1.55)

        ojo_izq_joven.move_to(cabeza_joven.get_center() + LEFT * 0.15 + UP * 0.05)
        ojo_der_joven.move_to(cabeza_joven.get_center() + RIGHT * 0.15 + UP * 0.05)

        joven = VGroup(
            cuerpo_joven,
            cabeza_joven,
            ojo_izq_joven,
            ojo_der_joven
        )

        # --- Persona mayor ---
        # Piel un poco más pálida/apagada que la del joven, cuerpo
        # con una ligera inclinación hacia adelante (encorvado), y
        # más detalles faciales (cejas, lentes, arrugas) para que se
        # lea claramente como una persona de edad avanzada, no solo
        # como el mismo personaje con otro color de cuerpo.

        cabeza_mayor = Circle(radius=0.46)
        cabeza_mayor.set_fill("#CBA37D", opacity=1)
        cabeza_mayor.set_stroke(width=2)

        cuerpo_mayor = RoundedRectangle(
            width=1.1,
            height=1.7,
            corner_radius=0.2
        )

        cuerpo_mayor.set_fill("#777777", opacity=1)
        cuerpo_mayor.set_stroke(width=2)

        cuerpo_mayor.move_to(RIGHT * 2.4 + DOWN * 1.5)

        # La cabeza se recarga un poco hacia abajo y al frente del
        # cuerpo, sugiriendo una postura encorvada por la edad
        cabeza_mayor.move_to(
            cuerpo_mayor.get_top() + UP * 0.4 + LEFT * 0.12
        )

        centro_cabeza = cabeza_mayor.get_center()

        # Cejas canosas
        ceja_izq = Arc(start_angle=PI * 0.85, angle=PI * 0.3, radius=0.16)
        ceja_der = Arc(start_angle=PI * -0.15, angle=PI * 0.3, radius=0.16)

        ceja_izq.move_to(centro_cabeza + LEFT * 0.15 + UP * 0.14)
        ceja_der.move_to(centro_cabeza + RIGHT * 0.15 + UP * 0.14)

        for ceja in (ceja_izq, ceja_der):
            ceja.set_stroke("#E8E8E8", width=3)

        # Ojos
        ojo_izq_mayor = Dot(radius=0.045, color=BLACK)
        ojo_der_mayor = Dot(radius=0.045, color=BLACK)

        ojo_izq_mayor.move_to(centro_cabeza + LEFT * 0.15 + UP * 0.02)
        ojo_der_mayor.move_to(centro_cabeza + RIGHT * 0.15 + UP * 0.02)

        # Lentes: dos aros delgados sobre los ojos, unidos por un puente
        lente_izq = Circle(radius=0.14)
        lente_der = Circle(radius=0.14)

        lente_izq.move_to(ojo_izq_mayor.get_center())
        lente_der.move_to(ojo_der_mayor.get_center())

        for lente in (lente_izq, lente_der):
            lente.set_stroke("#DDDDDD", width=2)
            lente.set_fill(opacity=0)

        puente_lentes = Line(
            lente_izq.get_right(),
            lente_der.get_left()
        )
        puente_lentes.set_stroke("#DDDDDD", width=2)

        # Arrugas pequeñas (patas de gallo) junto a cada ojo
        arruga_izq = Arc(start_angle=PI * 0.6, angle=PI * 0.35, radius=0.12)
        arruga_der = Arc(start_angle=PI * 0.05, angle=PI * 0.35, radius=0.12)

        arruga_izq.move_to(centro_cabeza + LEFT * 0.34 + DOWN * 0.02)
        arruga_der.move_to(centro_cabeza + RIGHT * 0.34 + DOWN * 0.02)

        for arruga in (arruga_izq, arruga_der):
            arruga.set_stroke("#9A7A58", width=1.5)

        # Boca, en una línea neutra y ligeramente curva
        boca = Arc(start_angle=PI * 1.15, angle=PI * 0.7, radius=0.17)
        boca.move_to(centro_cabeza + DOWN * 0.22)
        boca.set_stroke("#6B4A33", width=2)

        # Cabello cano: una "gorra" más amplia que cubre bien la
        # parte superior y los lados de la cabeza
        cabello = AnnularSector(
            inner_radius=0.38,
            outer_radius=0.5,
            angle=PI * 1.15,
            start_angle=PI * 0.92
        )

        cabello.move_to(centro_cabeza)
        cabello.set_fill("#F2F2F2", opacity=1)
        cabello.set_stroke("#F2F2F2", width=0)

        # Pequeño bastón para reforzar visualmente "mayor" sin
        # depender solo del color del cuerpo
        baston = Line(
            cuerpo_mayor.get_bottom() + RIGHT * 0.75,
            cuerpo_mayor.get_bottom() + RIGHT * 0.75 + UP * 1.15
        )
        baston.set_stroke("#C9C9C9", width=4)

        mano_baston = Dot(
            baston.get_end(),
            radius=0.07,
            color="#C9C9C9"
        )

        # Toda la cabeza y la cara se agrupan y se rotan juntas
        # (y no el círculo solo, que al ser simétrico no mostraría
        # ningún cambio visual) para lograr la inclinación encorvada
        cabeza_y_cara = VGroup(
            cabeza_mayor,
            cabello,
            ceja_izq,
            ceja_der,
            ojo_izq_mayor,
            ojo_der_mayor,
            lente_izq,
            lente_der,
            puente_lentes,
            arruga_izq,
            arruga_der,
            boca
        )

        cabeza_y_cara.rotate(-0.1, about_point=cuerpo_mayor.get_top())

        mayor = VGroup(
            cuerpo_mayor,
            cabeza_y_cara,
            baston,
            mano_baston
        )

        flecha_edad = Arrow(
            LEFT * 1.3 + DOWN * 1,
            RIGHT * 1.3 + DOWN * 1,
            buff=0,
            stroke_width=4
        )

        self.play(
            FadeIn(joven),
            run_time=0.8
        )

        self.play(
            Create(flecha_edad),
            FadeIn(mayor),
            run_time=1.5
        )

        joven_texto = Text("Juventud", font_size=22)
        mayor_texto = Text("Envejecimiento", font_size=22)

        joven_texto.next_to(cuerpo_joven, DOWN, buff=0.3)
        mayor_texto.next_to(cuerpo_mayor, DOWN, buff=0.3)

        self.play(
            FadeIn(joven_texto),
            FadeIn(mayor_texto),
            run_time=0.7
        )

        self.wait(2)

        self.play(
            FadeOut(texto_edad),
            FadeOut(joven),
            FadeOut(mayor),
            FadeOut(flecha_edad),
            FadeOut(joven_texto),
            FadeOut(mayor_texto),
            run_time=0.8
        )

        # ============================================================
        # ESCENA 4: LA FLECHA DEL TIEMPO (línea + barras de entropía)
        # ============================================================
        # Rediseño clave: las barras ahora comparten una misma línea
        # base (justo encima de la línea temporal) en lugar de estar
        # centradas en alturas distintas, que es lo que las hacía
        # verse "flotando" de forma inconsistente y chocar con la
        # etiqueta "Entropía" en la versión anterior.

        frase = VGroup(
            Text(
                "La entropía aumenta hacia el futuro.",
                font_size=29
            ),
            Text(
                "Eso define una dirección para el tiempo.",
                font_size=25
            )
        )

        frase.arrange(DOWN, buff=0.22)
        frase.next_to(titulo, DOWN, buff=0.55)

        self.play(
            FadeIn(frase),
            run_time=1
        )

        # Línea de tiempo principal
        linea_tiempo = Arrow(
            LEFT * 4.5,
            RIGHT * 4.5,
            buff=0,
            stroke_width=6
        )

        linea_tiempo.move_to(DOWN * 1.6)

        self.play(
            GrowArrow(linea_tiempo),
            run_time=1.5
        )

        # Puntos de tiempo, alineados exactamente sobre la línea
        pos_pasado = LEFT * 3.5 + DOWN * 1.6
        pos_presente = DOWN * 1.6
        pos_futuro = RIGHT * 3.5 + DOWN * 1.6

        pasado = Dot(pos_pasado, radius=0.12)
        presente = Dot(pos_presente, radius=0.12)
        futuro = Dot(pos_futuro, radius=0.12)

        pasado_label = Text("Pasado", font_size=21)
        presente_label = Text("Presente", font_size=21)
        futuro_label = Text("Futuro", font_size=21)

        pasado_label.next_to(pasado, DOWN, buff=0.25)
        presente_label.next_to(presente, DOWN, buff=0.25)
        futuro_label.next_to(futuro, DOWN, buff=0.25)

        self.play(
            FadeIn(pasado),
            FadeIn(presente),
            FadeIn(futuro),
            FadeIn(pasado_label),
            FadeIn(presente_label),
            FadeIn(futuro_label),
            run_time=1
        )

        # ------------------------------------------------------------
        # Barras de entropía: todas nacen desde la MISMA línea base,
        # justo encima de la línea temporal, y crecen hacia arriba.
        # ------------------------------------------------------------

        base_y = -1.6 + 0.35  # un pequeño espacio sobre la línea
        alturas = [0.6, 1.1, 1.8]
        posiciones_x = [pos_pasado[0], pos_presente[0], pos_futuro[0]]

        barras = VGroup()

        for x, h in zip(posiciones_x, alturas):

            barra = Rectangle(width=0.6, height=h)
            barra.set_fill(WHITE, opacity=0.7)
            barra.set_stroke(WHITE, width=2)

            # Se posiciona para que su BORDE INFERIOR quede en base_y,
            # así las tres comparten la misma línea de piso
            barra.move_to(
                np.array([x, base_y + h / 2, 0])
            )

            barras.add(barra)

        etiqueta_entropia = Text("Entropía", font_size=23)

        # Se coloca por encima de la barra más alta, con margen,
        # para que nunca quede tapada
        etiqueta_entropia.move_to(
            UP * (base_y + max(alturas) + 0.5)
        )

        self.play(
            FadeIn(etiqueta_entropia),
            run_time=0.6
        )

        for barra in barras:
            self.play(
                GrowFromEdge(barra, DOWN),
                run_time=0.7
            )

        # ============================================================
        # FRASE FINAL
        # ============================================================

        self.play(
            FadeOut(frase),
            FadeOut(etiqueta_entropia),
            FadeOut(pasado),
            FadeOut(presente),
            FadeOut(futuro),
            FadeOut(pasado_label),
            FadeOut(presente_label),
            FadeOut(futuro_label),
            FadeOut(barras),
            FadeOut(linea_tiempo),
            run_time=0.8
        )

        frase_final = VGroup(
            Text("A esto se le llama", font_size=25),
            Text("LA FLECHA DEL TIEMPO", font_size=36),
            Text("La entropía aumenta hacia el futuro.", font_size=24)
        )

        frase_final.arrange(DOWN, buff=0.25)
        frase_final.move_to(DOWN * 0.3)

        self.play(Write(frase_final[0]), run_time=0.7)
        self.play(Write(frase_final[1]), run_time=1)
        self.play(FadeIn(frase_final[2], shift=UP), run_time=0.8)

        self.wait(3)