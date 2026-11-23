# Natural-Language-Processing-with-Disaster-Tweets

Las redes sociales, y Twitter en particular, se han vuelto un canal de aviso en tiempo real durante emergencias: las personas reportan sismos, incendios o inundaciones antes de que lo hagan los medios. Agencias de ayuda humanitaria y de noticias quisieran monitorear esos mensajes de forma automática. El obstáculo es que el lenguaje es ambiguo: *"the sky is ablaze tonight"* puede describir un incendio real o un atardecer.

En este proyecto construimos y comparamos modelos de aprendizaje profundo (una CNN 1D y un Transformer preentrenado) frente a un modelo de referencia clásico (TF-IDF + Regresión Logística) para decidir si un tweet habla de un **desastre real**.
