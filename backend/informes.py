import subprocess


def exportar_informe(nombre_fichero):
    """Comprime un informe (VULNERABLE: inyección de comandos)."""
    subprocess.call("tar czf informes.tgz " + nombre_fichero, shell=True)
