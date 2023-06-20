# EMNGRadioButton 

## O componente JavaScript EMNGRadioButton é uma classe que encapsula a funcionalidade dos botões de rádio e fornece métodos para manipulá-los
---
### O construtor recebe um objeto options que contém várias opções de configuração para o componente.
---
### A propriedade this._options armazena as opções passadas para o construtor.
---
### O elemento pai do componente é obtido usando document.getElementById e armazenado em this._parent.
---
### Vários elementos HTML dentro do componente são selecionados e armazenados em propriedades para uso posterior, como this._inputTrue, this._inputFalse, this._grupo, this._labelTrue e this._labelFalse.

### Se a opção aoSelecionar for fornecida, os eventos de alteração dos botões de rádio são tratados chamando a função especificada por essa opção.
---
### Os métodos 
- ``aoSelecionar``
- ``obtenhaElTrue``
- ``selecione``
- ``selecioneTrue``
- ``selecioneFalse``
- ``desabilite``
- ``habilite``
- ``obtenhaSelecao``
- ``reset``
- ``definaRotuloTrue``
- ``definaRotuloFalse``
- ``addClassList``
- ``removeClassList``
### Fornecem diferentes funcionalidades para interagir com o componente.


# Agora, vamos analisar a relação entre o código JavaScript do componente e o código C# no arquivo .cshtml:

### Necessáriamente todas variáveis são definidas usando var e recebem valores do Html.ViewData.

---
### Um elemento `<div>` é gerado para renderizar o componente de botões de rádio personalizado.

---
### Dentro do elemento `<div>`, é feita uma verificação condicional para renderizar um elemento `<div>` adicional com uma etiqueta, dependendo do valor da variável rotuloOculto.

---
### Em seguida, um elemento `<div>` com a classe "btn-group" é renderizado para envolver os botões de rádio.

---
### Dois botões de rádio são renderizados usando elementos `<input>` com type="radio", e seus atributos são configurados com base nas variáveis e opções fornecidas.

---
### Os rótulos dos botões de rádio são renderizados usando elementos `<label>` com classes específicas.

---
### Por fim, um script JavaScript é gerado para criar uma instância do componente `EMNGRadioButton` usando as opções fornecidas.

---
# O builder EMNGRadioButtonsBuilder é usado para definir várias opções e configurações do componente.

## No método `WriteHtml` do builder, um dicionário de opções é criado com base nas propriedades do builder e em outros dados relacionados. Em seguida, é chamado um método `ObtenhaPartialView` para renderizar o componente de botões de rádio, passando o dicionário de opções como parâmetro.
---
## Em resumo, o componente JavaScript EMNGRadioButton fornece funcionalidade para interagir com botões de rádio personalizados, enquanto o código C# no arquivo .cshtml e no builder EMNGRadioButtonsBuilder facilitam a criação e renderização desse componente.

---
# Exemplos

```csharp

```
