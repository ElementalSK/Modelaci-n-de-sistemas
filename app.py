import streamlit as st


# Configuración de la página
#---------------------------------------
st.set_page_config(
    page_title="Sistema de Alerta Académica",
    page_icon="🎓",
    layout="wide",
)

# 🎨 Fondo general
#---------------------------------------
st.markdown("""
<style>
/* Fondo general de la app */
[data-testid="stAppViewContainer"] {
    background-color: #F4F6FA;
}

/* Sidebar con fondo blanco */
[data-testid="stSidebar"] {
    background-color: #FFFFFF;
}

/* Texto: párrafos y listas */
p, li {
    color: #1A1A1A !important;
    font-family: "Segoe UI", sans-serif;
    font-size: 17px;
}

/* Títulos más elegantes */
h1, h2, h3, h4 {
    color: #0A3C87 !important;
    font-family: "Segoe UI", sans-serif;
    font-weight: 700;
}
            
</style>
""", unsafe_allow_html=True)

# Loguitos
#-------------------------------------------
col_logo_izq, col_logo_centro, col_logo_der = st.columns([1, 6, 1])

with col_logo_izq:
    st.image("Logo UdeC.png", width=200)  # ajusta el nombre y tamaño

with col_logo_der:
    st.image("Logo FI.png", width=200)    


# Estilo personalizado para la SIDEBAR
#-------------------------------------------
st.markdown("""
<style>

/* SIDEBAR: fondo y título */
[data-testid="stSidebar"] {
    background-color: #E9EEF6 !important;  /* azul grisáceo suave */
    padding-top: 20px;
    padding-left: 15px;
}

[data-testid="stSidebar"] h2 {
    font-family: "Segoe UI", sans-serif;
    font-size: 1.3rem;
    font-weight: 700;
    color: #0A3C87;
    margin-bottom: 0.7rem;
}

/* Contenedor de las opciones del radio */
[data-testid="stSidebar"] .stRadio > div {
    display: flex;
    flex-direction: column;
    gap: 6px;
}

/* Cada opción del menú */
[data-testid="stSidebar"] .stRadio label {
    display: flex !important;
    align-items: center !important;
    gap: 8px !important;              /* espacio entre círculo y texto */
    padding: 4px 6px !important;
    border-radius: 12px;
    cursor: pointer;
    transition: 0.15s ease;
}

/* Texto de las opciones */
[data-testid="stSidebar"] .stRadio label p {
    margin: 0;
    font-size: 0.95rem;
    font-family: "Segoe UI", sans-serif;
    color: #1A1A1A;
}

/* Hover sobre la opción */
[data-testid="stSidebar"] .stRadio label:hover {
    background-color: rgba(10, 60, 135, 0.15);
}

/* === AQUÍ VIENE LA PARTE IMPORTANTE === */
/* Usamos el radio original, solo cambiamos color y tamaño */
[data-testid="stSidebar"] .stRadio input[type="radio"] {
    accent-color: #0A3C87;    /* color azul del punto */
    transform: scale(0.9);    /* un pelín más pequeño */
}

/* Opción seleccionada: pill azul con texto blanco */
[data-testid="stSidebar"] .stRadio input[type="radio"]:checked + div {
    background-color: #0A3C87;
    padding: 4px 10px;
    border-radius: 12px;
}

/* Texto de la opción seleccionada */
[data-testid="stSidebar"] .stRadio input[type="radio"]:checked + div p {
    color: #ffffff !important;
    font-weight: 600;
}

</style>
""", unsafe_allow_html=True)



# SIDEBAR
# ------------------------------------------

st.sidebar.title("Seleccione una página")

pagina = st.sidebar.radio(
    "",
    [
        "Inicio",
        "Usuario y Cliente",
        "Nuestra solución",
        "Cómo funciona el modelo",
        "Nuestro enfoque",
        "¿Quienes somos?"
    ],
)

# PÁGINAS
# ---------------------------
if pagina == "Inicio":
    st.title("Sistema de Alerta Académica Temprana")
    st.subheader("Un sistema preventivo para detectar riesgo académico")

    st.markdown(
        """
        Este proyecto surge desde la preocupación por la **detección tardía** del riesgo académico
        en estudiantes universitarios.  
        
        Nuestro objetivo es:

        - Identificar tempranamente a estudiantes con **mayor probabilidad de presentar dificultades académicas**.  
        - Entregar información clara y accionable a **tutores, psicólogos** y en general **encargados del bienestar estudiantil**.  
        - Favorecer **intervenciones preventivas**, antes de llegar a la deserción o a un deterioro severo del bienestar.

        Esta página está pensada como un **resumen explicativo del proyecto**,
        y tiene como misión informar cómo funcion el sistema y por qué fue diseñado de esta manera.
        """
    )

elif pagina == "Usuario y Cliente":
    st.header("Usuario y Cliente potencial")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Usuarios")
        st.markdown(
            """

            Los potenciales usuarios del sistema son aquellos profesionales encargados de acompañar y apoyar a los estudiantes dentro de la DISE, ya que, ellos son quienes
            interactuan directamente con situaciones de riesgo académico, socioemocinal o de bienestar. Entre ellos se consideran:

            - **Psicólogos/as DISE**  
              - Utilizarian las alertas para identificar que estudiantes presentan indicadores tempranos de desmotivacion, estrés académico o riesgo emocional. 

            - **Trabajadores/as sociales**  
              - Emplean las alertas para detectar casos asociados a dificultades socioeconómicas, acceso a beneficios y 
                situaciones personales que afectan el rendimiento académico.
                
            - **Profesionales de Bienestar Estudiantil** 
              - Monitorean patrones de riesgo académico y realizan derivaciones o intervenciones oportunas.

            - **Coordinadores/as de programas preventivos** (Por ejemplo, "UdeC Te Acompaña")  
              - Son aquellos que supervisan tendencias y activan protocolos de apoyo.

            """
        )

    with col2:
        
        st.image(
            "DISE UdeC.jpg",     
            caption="Dirección de Servicios Estudiantiles - UdeC",
            use_column_width=True)
        
    st.subheader("Cliente")
    st.markdown(
        """
        En el contexto actual nuestro cliente potencial corresponderia a: 

        - **Coordinacion Académica del programa**
            - Corresponde a los responsables de supervisar el progreso estudiantil y tomar decisiones institucionales
            para prevenir la deserción y rezago de los estudiantes.

            """
        )
    
elif pagina == "Nuestra solución":
    
    st.header("¿A qué problemas se enfrentan los estudiantes?")

    col1, col2 = st.columns([2.7,1.3])
    with col1:
        st.markdown("<br><br><br>", unsafe_allow_html=True)

        st.markdown(
            """
            En el contexto actual, tenemos las siguientes problemáticas:

            - Muchos estudiantes enfrentan problemas de rendimiento, desmotivacion o abandono académico, esto tiene 
            consecuencias negativas tanto para ellos como para la institución e incluso para el mercado laboral nacional.
        
            - Faltan herramientas efectivas para **identificar tempranamente** a los estudiantes en riesgo y alerten a las instituaciones antes de que los problemas se agraven.

            """
        )

    with col2:
        st.image(
            "Estudiante desmotivado.png",     
            caption="Estrés académico en estudiantes universitarios",
            width=450)
        

    st.subheader(" Nuestra solución")
    st.markdown(
        """
        Frente a este escenario, proponemos un **Sistema de Alerta Académica Temprana** que:

        - Analiza variables asociadas a la **trayectoria académica** y la **motivación**.  
        - Calcula un puntaje de riesgo para cada estudiante.  
        - Clasifica automáticamente a los alumnos en tres niveles de alerta

        """
    )

    st.markdown("""
    <style>
    .alert-card {
        background-color: #0A3C87;
        border-radius: 18px;
        padding: 25px 30px;
        color: white;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
        transition: transform 0.15s ease, box-shadow 0.15s ease;
    }
    .alert-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 8px 18px rgba(0,0,0,0.25);
    }
    .alert-title {
        font-size: 22px;
        font-weight: 700;
        margin-bottom: 10px;
    }
    .alert-body {
        font-size: 16px;
    }
    .circle-green {
        height: 18px;
        width: 18px;
        background-color: #20D03E;
        border-radius: 50%;
        display: inline-block;
        margin-right: 10px;
    }
    .circle-yellow {
        height: 18px;
        width: 18px;
        background-color: #FFD500;
        border-radius: 50%;
        display: inline-block;
        margin-right: 10px;
    }
    .circle-red {
        height: 18px;
        width: 18px;
        background-color: #FF3B30;
        border-radius: 50%;
        display: inline-block;
        margin-right: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

    colA, colB, colC = st.columns(3)

    with colA:
        st.markdown("""
        <div class="alert-card">
            <div class="alert-title">
                <span class="circle-green"></span> VERDE
            </div>
            <div class="alert-body">
                <b>Estado:</b> El estudiante va bien.<br>
                <b>Acción:</b> Monitoreo rutinario.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with colB:
        st.markdown("""
        <div class="alert-card">
            <div class="alert-title">
                <span class="circle-yellow"></span> AMARILLO
            </div>
            <div class="alert-body">
                <b>Estado:</b> Señales tempranas de dificultad.<br>
                <b>Acción:</b> Alerta a tutor.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with colC:
        st.markdown("""
        <div class="alert-card">
            <div class="alert-title">
                <span class="circle-red"></span> ROJO
            </div>
            <div class="alert-body">
                <b>Estado:</b> Dificultades graves.<br>
                <b>Acción:</b> Intervención inmediata.
            </div>
        </div>
        """, unsafe_allow_html=True)


    st.subheader("Variables consideradas en el diseño")
    st.markdown(
        """
        En esta etapa del proyecto, nos centramos en variables que son **fácilmente obtenibles y directamente relacionadas** 
        con el desempeño académico:

        """)

    col1, col2 = st.columns([2.7,1.3])

    with col1:
        st.markdown(
            """
        - **Cantidad de asignaturas reprobadas**  
          - Es uno de los indicadores más claros para visualizar de que manera se esta desempeñando academicamente un estudiante.  
            """)
    with col2:
        st.image(
            "Grafico Reprobacion.png", width=500)
    
    col1, col2 = st.columns([2.7,1.3])

    with col1:
        st.markdown(
            """

            - **Nivel de motivación actual** (autoinformado por el estudiante)  
                - Aporta una dimensión subjetiva clave: cómo se siente el estudiante frente a su carrera. Lo que nos permite captar tanto aspectos emocionales como actitudinales.  
            """
        )
        
    with col2:
        st.image(
            "Grafico motivacion.png", width=500)
        
    st.markdown(
        """
        - **Contexto individual** (carrera, género, ciudad de origen)  
          - Permite hacer análisis agregados y detectar posibles patrones de vulnerabilidad en ciertos grupos.
        """
    )
        

elif pagina == "Cómo funciona el modelo":
    st.header("¿En qué consiste nuestro modelo?")             
    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("En esta sección, explicaremos de que manera funciona tecnicamente la logica con la que opera nuestro sistema de alerta academica temprana.")
    st.markdown(""" 
                
    El código funciona basandose en el modelo de una **tubería de datos (Pipeline ETL)**, que consta de tres grandes etapas: Extracción de datos, 
                Transformacion y Carga en un reporte unificado. A continuación, se detalla cada una de estas etapas:

    """)


    st.markdown(
        """

        ### 1. Extracción de datos 
        El codigo procesa datos especificamente recopilados, aplicando filtros tal como:

        - **Filtro de Carreras**
             - El script contiene un "diccionario" con solamente 6 carreras seleccionadas que se consideran en el análisis. Estas son: Ingeniería Civil Industrial,
             Ingeniería Civil Eléctrica, Ingeniería Civil Electrónica, Ingeniería Civil Informática y Ingeniería Civil Comercial. 

        - **Filtro de admisión**
            - En el archivo Data_UINN_Facultad.csv, el código busca la columna Código Carrera Nacional. 
            Si el código de una fila no está en nuestra lista blanca (ej. 13072), esa fila se descarta inmediatamente.

        - **Filtro de Encuesta**
            - En el archivo Cuestionario...csv, el código busca la columna Carrera que estudias actualmente (que contiene códigos UDEC, ej. 3309). 
            Si el código no coincide con nuestra lista, se ignora.

        - **Filtro de "Datos Vacíos"**
            - Descarta estudiantes sin puntaje ponderado.
            - Descarta encuestas donde no se respondio la pregunta sobre motivación académica.

        Estos datos se almacenan en una base estructurada, que luego el programa en Python procesa.
        """
    )

    st.markdown(
        """
        ### 2. ¿Qué operaciones realiza? (La Transformación)

        El código realiza cálculos matemáticos para reducir miles de datos a indicadores manejables.

        ### A. En la Base de Admisión (Histórico)

        - **Limpieza:** Convierte los puntajes que usan coma (,) a punto (.) para que Python los entienda como números  
        _(ej: "650,5" → 650.5)_.

        - **Agregación (Promedio):** Agrupa a todos los estudiantes de una misma carrera y calcula el promedio de sus puntajes. Lo realiza mediante la siguiente operación:
        
        ```text             

        text{Promedio Puntajes} = frac{\\sum \\text{Puntajes Estudiantes}}{\\text{Total Estudiantes}}

        ```

        ### B. En la Base de Encuesta (Riesgo)

        - **Binarización (Creación de Bandera):** Transforma la respuesta de motivación (escala 1 a 5) en un 1 o un 0. La **Lógica** utilizada corresponde a: 
            - Si Motivación ≤ 2 (Bajo o Muy bajo) → **Asignar 1 (Riesgo)**.  
            - Si Motivación > 2 → **Asignar 0 (No riesgo)**.

        
        ### C. Cálculo de un puntaje de riesgo

        A partir de las respuestas, se calcula un **puntaje de riesgo académico**.  
        La lógica general es:

        - Más **asignaturas reprobadas** → **aumenta** el puntaje de riesgo.  
        - Mayor **motivación declarada** → **disminuye** el puntaje de riesgo.

        De forma esquemática:

        ```text             
        Puntaje de riesgo ≈ (1.5 × asignaturas reprobadas) – (0.5 × motivación)
        ```

        - Si el resultado es negativo, se reajusta a 0, ya que el puntaje negativo no tiene sentido en este contexto.
        - Los coeficientes (1.5 y 0.5) pueden ajustarse en función de análisis posteriores y validación con datos reales.
        """
    )
    
    st.markdown(
        """
        ### 3. ¿Cómo se compara las bases de datos? (El Cruce de datos)

        Esta parte corresponde a la más "inteligente" del script, deonde resolvemos la problematica de la falta de un ID común entre las bases de datos.

        ### **A. Traducción (El Mapeo)**

        El codigo toma la base de Admisión (que usa Códigos Nacionales, ej. 13072) y crea una columna "falsa" traduciéndolos a Códigos UDEC (ej. 3309) usando el PDF como diccionario3

        ### **B. El Match (Inner Join)**

        Usa la funcion pd.merge con el método inner.

        - Toma la tabla de "Promedios de Admisión" (Anteriormente traducida a código_UDEC).

        - Toma la tabla de "Porcentajes de Riesgo" (que ya usa código_UDEC).

        - Compara en ambas tablas en busca de que se cumple:

            ```text
            Codigo_UDEC_Admision == Codigo_UDEC_Encuesta
            ```
                
        - Si encuentra coincidencia, une ambas filas en una sola.

        - Si no encuentra coincidencia, descarta ambas filas.

        """
    )


    st.markdown(
        """
        ### 4. Transformación del puntaje en niveles de alerta

        Una vez calculado el puntaje de riesgo para cada estudiante, se analizan sus valores 
        a nivel de grupo (por ejemplo, cohorte o facultad) y se usan **percentiles** para separar en niveles:

        🟢 **Bajo riesgo:** estudiantes dentro del 70% con menor puntaje.  
        🟡 **Riesgo medio:** estudiantes entre el percentil 70 y 85.  
        🔴 **Alto riesgo:** estudiantes sobre el percentil 85.

        Esta forma de segmentar:

        - Permite identificar **un grupo priorizado de casos** donde el riesgo relativo es mayor.  
        - Evita depender de un umbral arbitrario fijo; se adapta a la distribución real de cada cohorte.
        """
    )

    st.markdown(
        """
        ### Rol del sistema

        El resultado final no es una “sentencia”, sino una **señal de alerta**:

        🟢 Bajo riesgo → monitoreo habitual.  
        🟡 Riesgo medio → seguimiento más cercano, posible derivación temprana.  
        🔴 Alto riesgo → recomendación de **intervención prioritaria** (tutorías, apoyo psicológico, etc.).

        Sin embargo, cabe recalcar que estos corresponden a sugerencias de nuestra parte, el objetivo es que nuestros usuarios y clientes,
        sean quienes tomen las decisiones finales, usando el sistema como herramienta de apoyo.
        """
    )

    st.markdown(
        """
        ### En resumen

        """
    )

    st.image(
        "Diagrama.jpeg",caption="Diagrama de flujo del sistema de alerta académica temprana", width=700)


elif pagina == "Nuestro enfoque":
    st.header("¿Por qué lo resolvimos de esta forma?")
    st.markdown(
        """
        Nuestro enfoque se basa en nuestro deseo de crear un sistema responsable, util y escalable a lo largo del tiempo.

        Para esto, nos guiamos en 4 principios clave:

        - **1. Privacidad**  
          - Se ocultan datos sensibles y evita entregar informacion a actores no pertinentes, como podria ser profesores o administrativos que no esten relacionados con el bienestar estudiantil.
        
        - **2. Proporcionalidad**  
            - Utilizamos unicamente variables necesarias para generar alertas significativas, evitando recopilar datos excesivos que puedan invadir la privacidad de los estudiantes o
          generar una mala medicion por un exceso de datos no relevantes.  
       
        - **3. Simplicidad**  
          - La interfaz es lineal, facil de interpretar y no requiere capacitacion especializada para su uso. Lo que facilita su adopcion por parte de los potenciales usuarios.

        - **4. Escabilidad**  
          - El modelo permite integrar nuevas cohortes, reajustar reglas del sistema e incluso conectar futuras herramientas de IA sin rediseñar desde cero.

        En resumen, nuestro objetivo es crear una herramienta práctica y efectiva que apoye a las instituciones educativas en su misión de acompañar a los estudiantes hacia el éxito académico.
        """
    )

   

elif pagina == "¿Quienes somos?":
    st.header("Equipo de trabajo")

    st.markdown(
        """
        **Grupo 27 – Modelación de Sistemas**

        - Sebastián Cárdenas Cabas  
        - Constanza Cartes Suazo  
        - Denisse Catrileo Retamal  
        - Martín Lara Loyola  
        - Estefanía Pezoa Zúñiga  
        - Felipe Sanhueza Díaz  
        
        ---
        Somos un grupo de estudiantes de Ingenieria Civil Industrial de la Universidad de Concepción, cursando la asignatura de Modelación de Sistemas
        en el segundo semestre de 2025. Nuestro interés radica en aplicar los conocimientos de la asignatura para resolver problematicas reales en el ambito académico.
        
        """
    )

    st.markdown("---")
    
