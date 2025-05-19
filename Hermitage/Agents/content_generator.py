from Hermitage.agents import Agent, function_tool
from Hermitage.core.config import get_llm_instance
from dotenv import load_dotenv
load_dotenv()
llm = get_llm_instance()



@function_tool
def generar_post_instagram(marca: str, producto: str) -> str:
    """Genera una publicación creativa de Instagram para un producto."""
    prompt = f"Redacta un post atractivo de Instagram para {marca}, promocionando su producto {producto}. Usa un tono informal y creativo."
    return llm.invoke(prompt)

@function_tool
def sugerir_nombre_campaña(objetivo: str, público_objetivo: str) -> str:
    """Sugiere un nombre creativo para una campaña de marketing."""
    prompt = f"Sugiere un nombre llamativo para una campaña cuyo objetivo es '{objetivo}' y está dirigida a '{público_objetivo}'."
    return llm.invoke(prompt)

@function_tool
def redactar_copy_promocional(producto: str, tono: str = "emocional") -> str:
    """Redacta un copy promocional breve para un producto en el tono indicado."""
    prompt = f"Escribe un copy de marketing para el producto '{producto}' en un tono {tono}."
    return llm.invoke(prompt)

@function_tool
def generar_guion_anuncio_tv(producto: str, duracion: str = "30 segundos") -> str:
    """Crea un guion para un anuncio de televisión breve y persuasivo."""
    prompt = f"Escribe un guion para un comercial de {duracion} sobre el producto '{producto}'. Sé emotivo, creativo y persuasivo."
    return llm.invoke(prompt)

@function_tool
def redactar_titulo_clickbait(tema: str) -> str:
    """Crea un título llamativo estilo clickbait para redes o artículos."""
    prompt = f"Escribe 3 títulos estilo clickbait sobre el siguiente tema: {tema}."
    return llm.invoke(prompt)

@function_tool
def crear_personaje_marca(nombre: str, personalidad: str) -> str:
    """Diseña un personaje que represente a la marca y conecte con el público."""
    prompt = f"Crea un personaje para la marca '{nombre}' con personalidad '{personalidad}'. Incluye su historia, tono y propósito comunicativo."
    return llm.invoke(prompt)

@function_tool
def generar_manifesto_marca(valores: str, visión: str) -> str:
    """Redacta un manifiesto que exprese la filosofía profunda de una marca."""
    prompt = f"Redacta un manifiesto de marca que refleje estos valores: {valores}, y esta visión: {visión}."
    return llm.invoke(prompt)

@function_tool
def proponer_segmento_creativo_producto(producto: str) -> str:
    """Propone un segmento de mercado creativo y poco convencional para el producto."""
    prompt = f"Propón un segmento de mercado no tradicional pero con alto potencial para el producto '{producto}'. Explica por qué puede funcionar."
    return llm.invoke(prompt)

@function_tool
def generar_carrusel_instagram(tema: str, num_slides: int = 5) -> str:
    """Crea ideas para un carrusel de Instagram educativo o inspirador."""
    prompt = f"Genera el contenido de {num_slides} slides para un carrusel de Instagram sobre: {tema}. Sé creativo, informativo y visual."
    return llm.invoke(prompt)

@function_tool
def traducir_contenido_multilenguaje(texto: str, idiomas: str = "inglés, francés") -> str:
    """Traduce un contenido publicitario a varios idiomas."""
    prompt = f"Traduce el siguiente contenido a estos idiomas ({idiomas}): {texto}"
    return llm.invoke(prompt)

@function_tool
def test_ab_campaña(version_a: str, version_b: str, objetivo: str) -> str:
    """Simula una evaluación A/B entre dos versiones de campaña."""
    prompt = f"Compara estas dos versiones de campaña para {objetivo}. Indica cuál puede ser más efectiva y por qué.\nVersión A: {version_a}\nVersión B: {version_b}"
    return llm.invoke(prompt)

@function_tool
def generar_hashtags_publicidad(tema: str, plataforma: str = "Instagram") -> str:
    """Sugiere hashtags relevantes y virales según el tema y la red social."""
    prompt = f"Sugiere una lista de hashtags efectivos para una campaña en {plataforma} sobre el tema: {tema}"
    return llm.invoke(prompt)

@function_tool
def adaptar_estilo_contenido(texto: str, estilo: str) -> str:
    """Adapta el contenido a un estilo creativo específico (ej. retro, minimalista)."""
    prompt = f"Reescribe este contenido en un estilo {estilo}: {texto}"
    return llm.invoke(prompt)

# Registrar el agente
agente_contenido = Agent(
    name="Agente Creativo Hermitage",
    instructions="Eres experto en contenido publicitario y marketing. Usa tus herramientas para generar ideas creativas.",
    tools=[
        generar_post_instagram,
        sugerir_nombre_campaña,
        redactar_copy_promocional,
        generar_guion_anuncio_tv,
        redactar_titulo_clickbait,
        crear_personaje_marca,
        generar_manifesto_marca,
        proponer_segmento_creativo_producto,
        generar_carrusel_instagram,
        traducir_contenido_multilenguaje,
        test_ab_campaña,
        generar_hashtags_publicidad,
        adaptar_estilo_contenido
    ]
)
