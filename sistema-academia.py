from controle.controlador_sistema import ControladorSistema

if __name__ == "__main__":
    controlador_sistema = ControladorSistema()
    controlador_sistema.instancia_planos()
    controlador_sistema.instancia_aparelhos()
    controlador_sistema.inicia()