from manim import *
import numpy as np


class EficienciaNaturaleza(Scene):

    def construct(self):

        # ============================================================
        # CONFIGURACIÓN
        # ============================================================

        self.camera.background_color = "#07080A"

        DORADO = "#D9A441"
        DORADO_CLARO = "#F2C866"
        AMARILLO = "#F2C14E"
        AMARILLO_CLARO = "#FFD966"
        VERDE = "#6FA85A"
        VERDE_OSCURO = "#31552C"
        MARRON = "#633B20"
        MARRON_OSCURO = "#29180E"
        CREMA = "#F4E3B2"
        AZUL = "#62B6E8"
        ROSA = "#E7A5B8"

        # ============================================================
        # FUNCIONES AUXILIARES
        # ============================================================

        def crear_petalos(centro, cantidad=28, radio=2.45):

            petalos = VGroup()

            largo, ancho = 1.7, 0.5
            radio_base = radio - largo / 2

            for i in range(cantidad):

                angulo = i * TAU / cantidad

                petalo = VMobject(
                    stroke_color="#C99520",
                    stroke_width=1
                )

                petalo.set_points_smoothly([
                    ORIGIN,
                    np.array([
                        ancho * 0.4,
                        largo * 0.3,
                        0
                    ]),
                    np.array([
                        ancho * 0.28,
                        largo * 0.75,
                        0
                    ]),
                    np.array([
                        0,
                        largo,
                        0
                    ]),
                    np.array([
                        -ancho * 0.28,
                        largo * 0.75,
                        0
                    ]),
                    np.array([
                        -ancho * 0.4,
                        largo * 0.3,
                        0
                    ]),
                    ORIGIN,
                ])

                petalo.set_fill(
                    color=[
                        AMARILLO,
                        AMARILLO_CLARO
                    ],
                    opacity=0.95
                )

                petalo.rotate(
                    angulo - PI / 2,
                    about_point=ORIGIN
                )

                petalo.shift(
                    centro
                    + radio_base * np.array([
                        np.cos(angulo),
                        np.sin(angulo),
                        0
                    ])
                )

                petalos.add(petalo)

            return petalos


        def crear_centro_girasol(centro):

            centro_girasol = VGroup()

            # --------------------------------------------------------
            # Disco principal
            # --------------------------------------------------------

            disco = Circle(
                radius=1.72,
                fill_color="#5A3A16",
                fill_opacity=1,
                stroke_color="#3A230D",
                stroke_width=3
            )

            disco.move_to(centro)

            centro_girasol.add(disco)

            # --------------------------------------------------------
            # Anillos
            # --------------------------------------------------------

            anillos = VGroup()

            for radio_anillo, opacidad in [
                (1.72, 0.25),
                (1.2, 0.2),
                (0.65, 0.15)
            ]:

                anillo = Circle(
                    radius=radio_anillo,
                    stroke_color="#2A1909",
                    stroke_width=6,
                    stroke_opacity=opacidad,
                    fill_opacity=0
                )

                anillo.move_to(centro)

                anillos.add(anillo)

            centro_girasol.add(anillos)

            # --------------------------------------------------------
            # Semillas
            # --------------------------------------------------------

            semillas = VGroup()

            angulo_dorado = 137.507764 * DEGREES

            np.random.seed(10)

            for i in range(1, 430):

                r = 0.075 * np.sqrt(i)

                r += np.random.uniform(
                    -0.012,
                    0.012
                )

                theta = i * angulo_dorado

                x = r * np.cos(theta)
                y = r * np.sin(theta)

                x *= 1.02
                y *= 0.98

                ancho_semilla = np.random.uniform(
                    0.035,
                    0.06
                )

                largo_semilla = (
                    ancho_semilla
                    * np.random.uniform(
                        1.8,
                        2.3
                    )
                )

                semilla = Ellipse(
                    width=ancho_semilla,
                    height=largo_semilla,
                    fill_opacity=1,
                    stroke_width=0,
                    color=np.random.choice([
                        "#D69B2D",
                        "#E6B94A",
                        "#B9791E",
                        "#F0C85C",
                        "#8F5D19"
                    ])
                )

                semilla.rotate(
                    theta + PI / 2
                )

                semilla.move_to(
                    centro
                    + np.array([
                        x,
                        y,
                        0
                    ])
                )

                semillas.add(semilla)

            centro_girasol.add(semillas)

            # --------------------------------------------------------
            # Centro pequeño
            # --------------------------------------------------------

            centro_girasol.add(
                Dot(
                    point=centro,
                    radius=0.12,
                    color="#2A1909"
                )
            )

            return centro_girasol


        def crear_escama(
            ancho,
            alto,
            color_relleno,
            color_sombra,
            color_borde
        ):

            escama = VMobject(
                stroke_color=color_borde,
                stroke_width=1.2
            )

            escama.set_points_smoothly([
                np.array([
                    0,
                    alto * 0.5,
                    0
                ]),
                np.array([
                    ancho * 0.42,
                    alto * 0.12,
                    0
                ]),
                np.array([
                    ancho * 0.32,
                    alto * -0.28,
                    0
                ]),
                np.array([
                    0,
                    alto * -0.38,
                    0
                ]),
                np.array([
                    -ancho * 0.32,
                    alto * -0.28,
                    0
                ]),
                np.array([
                    -ancho * 0.42,
                    alto * 0.12,
                    0
                ]),
                np.array([
                    0,
                    alto * 0.5,
                    0
                ]),
            ])

            escama.set_fill(
                color=[
                    color_relleno,
                    color_sombra
                ],
                opacity=1
            )

            return escama


        # ============================================================
        # PIÑA DE CONÍFERA
        # ============================================================

        def crear_pina(centro):

            pina = VGroup()

            # --------------------------------------------------------
            # Cuerpo principal
            # --------------------------------------------------------

            cuerpo = Ellipse(
                width=2.25,
                height=4.0,
                fill_color="#6B4325",
                fill_opacity=1,
                stroke_color="#3A2112",
                stroke_width=3
            )

            cuerpo.move_to(centro)

            pina.add(cuerpo)

            # --------------------------------------------------------
            # Escamas
            # --------------------------------------------------------

            escamas = VGroup()

            filas = 8

            for fila in range(filas):

                y = -1.55 + fila * 0.43

                factor = max(
                    0.15,
                    1 - (y / 2.0) ** 2
                )

                ancho = (
                    1.65
                    * np.sqrt(factor)
                )

                cantidad = (
                    5
                    if fila % 2 == 0
                    else 6
                )

                factor_sombra = (
                    fila / (filas - 1)
                )

                color_relleno = interpolate_color(
                    ManimColor("#B98545"),
                    ManimColor("#7A4D22"),
                    factor_sombra
                )

                color_sombra = interpolate_color(
                    ManimColor("#8A5A28"),
                    ManimColor("#4A2A12"),
                    factor_sombra
                )

                for j in range(cantidad):

                    if cantidad == 1:
                        x = 0
                    else:
                        x = (
                            -ancho / 2
                            + j * ancho
                            / (cantidad - 1)
                        )

                    escama = crear_escama(
                        0.55,
                        0.46,
                        color_relleno,
                        color_sombra,
                        "#4A2A17"
                    )

                    escama.move_to(
                        centro
                        + np.array([
                            x,
                            y,
                            0
                        ])
                    )

                    escamas.add(escama)

            pina.add(escamas)

            # --------------------------------------------------------
            # Corona superior
            # --------------------------------------------------------

            hojas = VGroup()

            for i in range(10):

                angulo = (
                    -PI / 2
                    + (i - 4.5) * 0.23
                )

                hoja = Ellipse(
                    width=0.22,
                    height=0.95,
                    fill_color=VERDE_OSCURO,
                    fill_opacity=1,
                    stroke_color=VERDE,
                    stroke_width=1
                )

                hoja.rotate(angulo)

                hoja.move_to(
                    centro
                    + UP * 1.98
                    + RIGHT * (
                        (i - 4.5)
                        * 0.16
                    )
                )

                hojas.add(hoja)

            pina.add(hojas)

            return pina


        # ============================================================
        # PIÑA TROPICAL
        # ============================================================

        def crear_pina_tropical(centro):

            fruta = VGroup()

            # --------------------------------------------------------
            # Cuerpo
            # --------------------------------------------------------

            cuerpo = Ellipse(
                width=2.15,
                height=3.0,
                fill_color="#D5A52F",
                fill_opacity=1,
                stroke_color="#8E6918",
                stroke_width=3
            )

            cuerpo.move_to(centro)

            fruta.add(cuerpo)

            # --------------------------------------------------------
            # Romboides
            # --------------------------------------------------------

            patrones = VGroup()

            filas = 7

            for fila in range(filas):

                y = -1.02 + fila * 0.34

                factor = max(
                    0.20,
                    1 - (y / 1.5) ** 2
                )

                ancho = (
                    0.82
                    * np.sqrt(factor)
                )

                cantidad = 5

                for j in range(cantidad):

                    separacion = (
                        2 * ancho
                        / (cantidad - 1)
                    )

                    x = (
                        -ancho
                        + j * separacion
                    )

                    if fila % 2 == 1:
                        x += (
                            separacion * 0.5
                        )

                    if abs(x) > ancho:
                        continue

                    factor_sombra = (
                        fila
                        / (filas - 1)
                    )

                    color_celda = interpolate_color(
                        ManimColor("#E3B84A"),
                        ManimColor("#B9861E"),
                        factor_sombra
                    )

                    rombo = Polygon(
                        np.array([
                            0,
                            0.16,
                            0
                        ]),
                        np.array([
                            0.17,
                            0,
                            0
                        ]),
                        np.array([
                            0,
                            -0.16,
                            0
                        ]),
                        np.array([
                            -0.17,
                            0,
                            0
                        ]),
                        fill_color=color_celda,
                        fill_opacity=0.55,
                        stroke_color="#8B681D",
                        stroke_width=1.2
                    )

                    rombo.move_to(
                        centro
                        + np.array([
                            x,
                            y,
                            0
                        ])
                    )

                    patrones.add(rombo)

            fruta.add(patrones)

            # --------------------------------------------------------
            # Corona de hojas
            # --------------------------------------------------------

            corona = VGroup()

            for i in range(11):

                desplazamiento = i - 5

                angulo = (
                    -PI / 2
                    + desplazamiento * 0.18
                )

                hoja = Ellipse(
                    width=0.20,
                    height=1.30,
                    fill_color=VERDE,
                    fill_opacity=1,
                    stroke_color=VERDE_OSCURO,
                    stroke_width=1
                )

                hoja.rotate(angulo)

                hoja.move_to(
                    centro
                    + UP * 1.58
                    + RIGHT * (
                        desplazamiento
                        * 0.14
                    )
                )

                corona.add(hoja)

            fruta.add(corona)

            return fruta


        # ============================================================
        # ESPIRAL
        # ============================================================

        def crear_espiral(
            centro,
            rotaciones,
            direccion=1,
            escala=0.075,
            color=CREMA,
            grosor=2.2
        ):

            puntos = []

            cantidad = 140

            for i in range(cantidad):

                t = (
                    i / (cantidad - 1)
                ) * rotaciones * TAU

                r = escala * t

                theta = (
                    direccion * t
                )

                x = r * np.cos(theta)
                y = r * np.sin(theta)

                puntos.append(
                    centro
                    + np.array([
                        x,
                        y,
                        0
                    ])
                )

            curva = VMobject()

            curva.set_points_smoothly(
                puntos
            )

            curva.set_stroke(
                color=color,
                width=grosor,
                opacity=0.85
            )

            return curva


        # ============================================================
        # 1. TÍTULO
        # ============================================================

        titulo = Text(
            "Espirales de Fibonacci en la Naturaleza",
            font_size=31,
            color=WHITE
        )

        titulo.to_edge(
            UP,
            buff=0.35
        )

        subtitulo = Text(
            "34 espirales en un sentido • 55 en el otro",
            font_size=19,
            color=DORADO_CLARO
        )

        subtitulo.next_to(
            titulo,
            DOWN,
            buff=0.18
        )

        self.play(
            Write(titulo),
            FadeIn(subtitulo),
            run_time=1.5
        )

        self.wait(0.7)

        # ============================================================
        # 2. GIRASOL
        # ============================================================

        centro_girasol = DOWN * 0.45

        petalos = crear_petalos(
            centro_girasol
        )

        centro_semillas = crear_centro_girasol(
            centro_girasol
        )

        self.play(
            LaggedStart(
                *[
                    FadeIn(
                        p,
                        scale=0.7
                    )
                    for p in petalos
                ],
                lag_ratio=0.025
            ),
            run_time=2.5
        )

        self.play(
            FadeIn(
                centro_semillas,
                scale=0.85
            ),
            run_time=2
        )

        ejemplos = Text(
            "Girasoles",
            font_size=20,
            color=GRAY_A
        )

        ejemplos.to_edge(
            DOWN,
            buff=0.35
        )

        self.play(
            FadeIn(ejemplos),
            run_time=0.8
        )

        self.wait(1.5)

        # ============================================================
        # 3. ESPIRALES DEL GIRASOL
        # ============================================================

        self.play(
            FadeOut(subtitulo),
            run_time=0.5
        )

        texto_espirales = Text(
            "Las semillas forman patrones espirales visibles",
            font_size=22,
            color=WHITE
        )

        texto_espirales.to_edge(
            UP,
            buff=0.9
        )

        self.play(
            FadeIn(texto_espirales),
            run_time=0.8
        )

        espirales_1 = VGroup()
        espirales_2 = VGroup()

        for k in range(7):

            esp = crear_espiral(
                centro_girasol,
                rotaciones=2.4,
                direccion=1,
                escala=0.105,
                color="#F7D36B",
                grosor=1.6
            )

            esp.rotate(
                k * 0.13
            )

            espirales_1.add(esp)

        for k in range(7):

            esp = crear_espiral(
                centro_girasol,
                rotaciones=2.15,
                direccion=-1,
                escala=0.115,
                color="#58B6E8",
                grosor=1.6
            )

            esp.rotate(
                k * 0.13
            )

            espirales_2.add(esp)

        contador_34 = Text(
            "34",
            font_size=30,
            color="#58B6E8"
        )

        texto_34 = Text(
            "espirales",
            font_size=17,
            color="#58B6E8"
        )

        grupo_34 = VGroup(
            contador_34,
            texto_34
        ).arrange(
            DOWN,
            buff=0.02
        )

        grupo_34.to_edge(
            LEFT,
            buff=0.35
        )

        grupo_34.shift(
            DOWN * 0.35
        )

        contador_55 = Text(
            "55",
            font_size=30,
            color="#F7D36B"
        )

        texto_55 = Text(
            "espirales",
            font_size=17,
            color="#F7D36B"
        )

        grupo_55 = VGroup(
            contador_55,
            texto_55
        ).arrange(
            DOWN,
            buff=0.02
        )

        grupo_55.to_edge(
            RIGHT,
            buff=0.35
        )

        grupo_55.shift(
            DOWN * 0.35
        )

        self.play(
            Create(espirales_1),
            Create(espirales_2),
            FadeIn(grupo_34),
            FadeIn(grupo_55),
            run_time=2.5
        )

        self.wait(2)

        # ============================================================
        # 4. TRANSICIÓN
        # ============================================================

        self.play(
            FadeOut(titulo),
            FadeOut(petalos),
            FadeOut(centro_semillas),
            FadeOut(espirales_1),
            FadeOut(espirales_2),
            FadeOut(grupo_34),
            FadeOut(grupo_55),
            FadeOut(texto_espirales),
            FadeOut(ejemplos),
            run_time=1.2
        )

        # ============================================================
        # 5. PIÑA Y PIÑA TROPICAL
        # ============================================================

        titulo_ejemplos = Text(
            "El mismo tipo de patrón aparece en otras plantas",
            font_size=25,
            color=WHITE
        )

        titulo_ejemplos.to_edge(
            UP,
            buff=0.55
        )

        self.play(
            Write(titulo_ejemplos),
            run_time=1
        )

        # ------------------------------------------------------------
        # Posiciones corregidas
        # ------------------------------------------------------------

        centro_pina = (
            LEFT * 2.15
            + DOWN * 0.35
        )

        centro_pina_tropical = (
            RIGHT * 2.15
            + DOWN * 0.35
        )

        pina = crear_pina(
            centro_pina
        )

        pina_tropical = crear_pina_tropical(
            centro_pina_tropical
        )

        # ------------------------------------------------------------
        # Etiquetas
        # ------------------------------------------------------------

        etiqueta_pina = Text(
            "Escamas de una piña",
            font_size=17,
            color=CREMA
        )

        etiqueta_pina.next_to(
            pina,
            DOWN,
            buff=0.45
        )

        etiqueta_tropical = Text(
            "Piña tropical",
            font_size=17,
            color=DORADO_CLARO
        )

        etiqueta_tropical.next_to(
            pina_tropical,
            DOWN,
            buff=0.45
        )

        self.play(
            FadeIn(
                pina,
                scale=0.8
            ),
            FadeIn(
                pina_tropical,
                scale=0.8
            ),
            run_time=2
        )

        self.play(
            FadeIn(etiqueta_pina),
            FadeIn(etiqueta_tropical),
            run_time=1
        )

        self.wait(2)

        # ============================================================
        # 6. ESPIRALES EN LA PIÑA
        # ============================================================

        espiral_pina_1 = VGroup()
        espiral_pina_2 = VGroup()

        for k in range(4):

            esp = crear_espiral(
                centro_pina,
                rotaciones=1.75,
                direccion=1,
                escala=0.085,
                color="#62B6E8",
                grosor=1.5
            )

            esp.scale(0.82)

            esp.shift(
                RIGHT * (k - 1.5) * 0.13
                + UP * (k - 1.5) * 0.02
            )

            espiral_pina_1.add(esp)

        for k in range(4):

            esp = crear_espiral(
                centro_pina,
                rotaciones=1.65,
                direccion=-1,
                escala=0.09,
                color="#F2C14E",
                grosor=1.5
            )

            esp.scale(0.82)

            esp.shift(
                LEFT * (k - 1.5) * 0.13
                + DOWN * (k - 1.5) * 0.02
            )

            espiral_pina_2.add(esp)

        texto_pina = Text(
            "Las escamas también forman espirales",
            font_size=20,
            color=WHITE
        )

        texto_pina.to_edge(
            UP,
            buff=1.15
        )

        self.play(
            Create(espiral_pina_1),
            Create(espiral_pina_2),
            FadeIn(texto_pina),
            run_time=2
        )

        self.wait(2)

        # ============================================================
        # 7. ¿POR QUÉ PASA ESTO?
        # ============================================================

        self.play(
            FadeOut(pina),
            FadeOut(pina_tropical),
            FadeOut(etiqueta_pina),
            FadeOut(etiqueta_tropical),
            FadeOut(espiral_pina_1),
            FadeOut(espiral_pina_2),
            FadeOut(texto_pina),
            FadeOut(titulo_ejemplos),
            run_time=1.2
        )

        pregunta = Text(
            "¿Por qué pasa esto?",
            font_size=35,
            color=ROSA
        )

        pregunta.shift(
            UP * 1.25
        )

        respuesta1 = Text(
            "No es magia ni coincidencia mística.",
            font_size=23,
            color=GRAY_B
        )

        respuesta1.next_to(
            pregunta,
            DOWN,
            buff=0.4
        )

        respuesta2 = Text(
            "Es EFICIENCIA.",
            font_size=42,
            color=GREEN_B
        )

        respuesta2.next_to(
            respuesta1,
            DOWN,
            buff=0.45
        )

        self.play(
            Write(pregunta),
            run_time=1
        )

        self.wait(0.5)

        self.play(
            FadeIn(respuesta1),
            run_time=1
        )

        self.play(
            Write(respuesta2),
            run_time=1.2
        )

        self.wait(1.8)

        # ============================================================
        # 8. APROVECHAMIENTO DEL ESPACIO
        # ============================================================

        self.play(
            FadeOut(pregunta),
            FadeOut(respuesta1),
            respuesta2.animate
                .to_edge(
                    UP,
                    buff=0.75
                )
                .scale(0.8),
            run_time=1
        )

        puntos = VGroup(

            Text(
                "Máximo aprovechamiento de la luz solar\n"
                "y del espacio.",
                font_size=20,
                color=WHITE,
                line_spacing=1.2
            ),

            Text(
                "Las semillas se distribuyen evitando\n"
                "grandes espacios vacíos.",
                font_size=20,
                color=WHITE,
                line_spacing=1.2
            ),

            Text(
                "Así, muchas semillas pueden crecer\n"
                "sin desperdiciar espacio.",
                font_size=20,
                color=GOLD,
                line_spacing=1.2
            )

        ).arrange(
            DOWN,
            aligned_edge=LEFT,
            buff=0.40
        )

        puntos.move_to(
            DOWN * 0.1
        )

        self.play(
            LaggedStart(
                *[
                    Write(p)
                    for p in puntos
                ],
                lag_ratio=0.45
            ),
            run_time=3
        )

        self.wait(2)

        # ============================================================
        # 9. ÁNGULO DORADO
        # ============================================================

        self.play(
            FadeOut(puntos),
            FadeOut(respuesta2),
            run_time=1
        )

        titulo_angulo = Text(
            "El ángulo dorado",
            font_size=30,
            color=DORADO_CLARO
        )

        titulo_angulo.to_edge(
            UP,
            buff=0.6
        )

        # ------------------------------------------------------------
        # Diagrama
        # ------------------------------------------------------------

        linea1 = Line(
            LEFT * 2.0,
            LEFT * 0.7,
            color=WHITE,
            stroke_width=4
        )

        linea2 = Line(
            LEFT * 2.0,
            LEFT * 2.0
            + 1.25 * np.array([
                np.cos(
                    137.5 * DEGREES
                ),
                np.sin(
                    137.5 * DEGREES
                ),
                0
            ]),
            color=DORADO_CLARO,
            stroke_width=4
        )

        angulo = Arc(
            radius=0.65,
            start_angle=0,
            angle=137.5 * DEGREES,
            color=DORADO_CLARO,
            stroke_width=5
        ).move_to(
            LEFT * 2.0
        )

        numero_angulo = Text(
            "≈ 137,5°",
            font_size=30,
            color=DORADO_CLARO
        )

        numero_angulo.next_to(
            angulo,
            RIGHT,
            buff=0.30
        )

        # ------------------------------------------------------------
        # Explicación
        # ------------------------------------------------------------

        explicacion = Text(
            "Este ángulo permite que las semillas,\n"
            "hojas y ramas se distribuyan de forma\n"
            "muy eficiente, evitando desperdiciar espacio.",
            font_size=19,
            color=WHITE,
            line_spacing=1.25
        )

        explicacion.to_edge(
            RIGHT,
            buff=0.45
        )

        explicacion.shift(
            DOWN * 0.15
        )

        self.play(
            Write(titulo_angulo),
            Create(linea1),
            Create(linea2),
            Create(angulo),
            Write(numero_angulo),
            FadeIn(explicacion),
            run_time=2.5
        )

        self.wait(2)

        # ============================================================
        # 10. EVOLUCIÓN
        # ============================================================

        self.play(
            FadeOut(titulo_angulo),
            FadeOut(linea1),
            FadeOut(linea2),
            FadeOut(angulo),
            FadeOut(numero_angulo),
            FadeOut(explicacion),
            run_time=1
        )

        conclusion1 = Text(
            'La naturaleza no "conoce" a Fibonacci.',
            font_size=27,
            color=AZUL
        )

        conclusion1.shift(
            UP * 0.9
        )

        conclusion2 = Text(
            "La evolución fue favoreciendo, generación tras generación,\n"
            "a las plantas que lograban distribuir mejor sus semillas y hojas.",
            font_size=21,
            color=WHITE,
            line_spacing=1.3
        )

        conclusion2.next_to(
            conclusion1,
            DOWN,
            buff=0.5
        )

        self.play(
            Write(conclusion1),
            run_time=1.5
        )

        self.wait(0.5)

        self.play(
            FadeIn(
                conclusion2,
                shift=UP * 0.2
            ),
            run_time=2
        )

        self.wait(3)

        self.play(
            FadeOut(conclusion1),
            FadeOut(conclusion2),
            run_time=1
        )

        # ============================================================
        # 11. CIERRE
        # ============================================================

        cierre = Text(
            "Matemáticas que aparecen en la naturaleza.",
            font_size=26,
            color=DORADO_CLARO
        )

        cierre.to_edge(
            DOWN,
            buff=0.45
        )

        self.play(
            FadeIn(cierre),
            run_time=1
        )

        self.wait(2)