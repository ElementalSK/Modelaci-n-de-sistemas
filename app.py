import streamlit as st


# CONFIGURACIÓN GENERAL DE LA PÁGINA
#---------------------------------------
st.set_page_config(
    page_title="Sistema de Alerta Académica",
    page_icon="🎓",
    layout="wide",
)

# SIDEBAR: NAVEGACIÓN
# ------------------------------------------

st.sidebar.title("Navegación")

pagina = st.sidebar.radio(
    "Selecciona una página:",
    [
        "Inicio",
        "Usuario y problema",
        "Nuestra solución",
        "Cómo funciona el modelo",
        "Por qué este enfoque",
        "¿Quienes somos?"
    ],
)

# PÁGINAS
# ---------------------------
if pagina == "Inicio":
    st.title("🎓 Sistema de Alerta Académica Temprana")
    st.subheader("Un sistema preventivo para detectar riesgo académico")

    st.markdown(
        """
        Este proyecto surge desde la preocupación por la **detección tardía** del riesgo académico
        en estudiantes universitarios.  
        
        Nuestro objetivo es:

        - Identificar tempranamente a estudiantes con **mayor probabilidad de presentar dificultades académicas**.  
        - Entregar información clara y accionable a **tutores, psicólogos y jefes de carrera**.  
        - Favorecer **intervenciones preventivas**, antes de llegar a la deserción o a un deterioro severo del bienestar.

        Esta página está pensada como un **resumen explicativo del proyecto**,
        y tiene como misión informar cómo funcion el sistema y por qué fue diseñado de esta manera.
        """
    )

elif pagina == "Usuario y problema":
    st.header("👥 ¿Quién es el usuario y cuál es el problema?")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Usuarios principales")
        st.markdown(
            """

            - **Estudiantes universitarios**  
              - Son quienes viven directamente las consecuencias del riesgo académico
                (reprobaciones, desmotivación, estrés, posible deserción).  
            - **Tutores académicos**  
              - Requieren señales tempranas para saber que estudiante se encuentren en riesgo
                con el fin de brindar apoyo oportuno.
            - **Unidades de apoyo estudiantil** 
              - Necesitan indicadores claros para priorizar intervenciones en salud mental. 
            - **Jefes de carrera y autoridades académicas**  
              - Buscan reducir reprobación y deserción, y mejorar el bienestar estudiantil con decisiones basadas en datos.
            """
        )

    with col2:
        st.subheader("¿A qué problema se enfrentan?")
        st.markdown(
            """
            En el contexto actual:

            - El **riesgo académico suele detectarse demasiado tarde**, cuando el estudiante ya acumula varias reprobaciones y esta en riesgo su continuidad en la carrera.  
            - No siempre hay una herramienta simple y clara que muestre que estudiantes se encuentran con mayor vulnerabilidad durante el semestre. 

            Esto se traduce en:

            - Mayor probabilidad de **deserción**.  
            - Sobrecarga para equipos de apoyo, que realizan más trabajo reactivo que preventivo. 
            - Impacto directo en el bienestar emocional del estudiante.
            """
        )

elif pagina == "Nuestra solución":
    st.header(" Nuestra solución")

    st.markdown(
        """
        Frente a este escenario, proponemos un **Sistema de Alerta Académica Temprana** que:

        - Analiza variables asociadas a la **trayectoria académica** y la **motivación**.  
        - Calcula un puntaje de riesgo para cada estudiante.  
        - Clasifica automáticamente a los alumnos en uno de los tres siguientes niveles de alerta:

          - 🟢 **Bajo riesgo**  
          - 🟡 **Riesgo medio**  
          - 🔴 **Alto riesgo**  

        El foco del sistema es **preventivo**:

        - Busca **visibilizar a tiempo** qué casos podrían requerir acompañamiento adicional.
        """
    )

    st.subheader("Variables consideradas en el diseño")
    st.markdown(
        """
        En esta etapa del proyecto, nos centramos en variables que son **fácilmente obtenibles y directamente relacionadas** 
        con el desempeño académico:

        - **Cantidad de asignaturas reprobadas**  
          - Es uno de los indicadores más claros de dificultades académicas acumuladas.  
        - **Nivel de motivación actual** (autoinformado por el estudiante)  
          - Aporta una dimensión subjetiva clave: cómo se siente el estudiante frente a su carrera.  
        - **Contexto** (carrera, género, ciudad de origen)  
          - Permite hacer análisis agregados y detectar posibles patrones de vulnerabilidad en ciertos grupos.

        """
    )

elif pagina == "Cómo funciona el modelo":
    st.header("¿En qué consiste nuestro modelo?")             

    st.markdown(
        """
        El modelo está pensado como un **primer MVP** (Producto Mínimo Viable), 
        enfocado en la **simplicidad y la interpretabilidad**.

        ### 1. Recopilación de datos
        La universidad recoge información mediante un **cuestionario** que incluye, entre otros:

        - Número de asignaturas reprobadas hasta la fecha.  
        - Nivel de motivación por estudiar la carrera (en una escala, por ejemplo, de 1 a 5).  
        - Datos de contexto (carrera, género, ciudad de origen, etc.).

        Estos datos se almacenan en una base estructurada, que luego el programa en Python procesa.
        """
    )

    st.markdown(
        """
        ### 2. Cálculo de un puntaje de riesgo

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
        ### 3. Transformación del puntaje en niveles de alerta

        Una vez calculado el puntaje de riesgo para cada estudiante, se analizan sus valores 
        a nivel de grupo (por ejemplo, cohorte o facultad) y se usan **percentiles** para separar en niveles:

        - 🟢 **Bajo riesgo:** estudiantes dentro del 70% con menor puntaje.  
        - 🟡 **Riesgo medio:** estudiantes entre el percentil 70 y 85.  
        - 🔴 **Alto riesgo:** estudiantes sobre el percentil 85.

        Esta forma de segmentar:

        - Permite identificar **un grupo priorizado de casos** donde el riesgo relativo es mayor.  
        - Evita depender de un umbral arbitrario fijo; se adapta a la distribución real de cada cohorte.
        """
    )

    st.markdown(
        """
        ### 4. Rol del sistema

        El resultado final no es una “sentencia”, sino una **señal de alerta**:

        - 🟢 Bajo riesgo → monitoreo habitual.  
        - 🟡 Riesgo medio → seguimiento más cercano, posible derivación temprana.  
        - 🔴 Alto riesgo → recomendación de **intervención prioritaria** (tutorías, apoyo psicológico, etc.).

        Sin embargo, cabe recalcar que estos corresponden a sugerencias de nuestra parte, el objetivo es que nuestros usuarios y clientes,
        sean quienes tomen las decisiones finales, usando el sistema como herramienta de apoyo.
        """
    )

elif pagina == "Por qué este enfoque":
    st.header("¿Por qué lo resolvimos de esta forma?")

   

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
      (Explicacion de que somos estudiante de industrial y eso)
        """
    )

    st.markdown("---")
    
