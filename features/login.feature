# language: pt
Funcionalidade: Testar a funcionalidade de login do ERP Vhsys

  Esquema do Cenário: Tentativa de acesso sem credenciais
    Dado o navegador "<navegador>"
    E a tela de login do vhsys
    Quando clicado no botão entrar
    Então deve apresentar a mensagem "Informe o login e a senha!"

    Exemplos:
      |navegador|
      |Chrome   |
      |Firefox  |

  Cenário: Tentativa de acesso com credenciais corretas
    Dado o navegador "Chrome"
    E o usuário está logado no sistema
    Então deve apresentar o elemento "logo-avatar-mini" com o atributo "src" contendo o valor "https://app.vhsys.com.br/empresa/logo/1"