# ReAct Model 

Este projeto demonstra uma simulação simples de como um modelo de linguagem pode utilizar a abordagem ReAct (Reasoning and Acting) para gerar código Python a partir de um prompt de entrada. A abordagem ReAct combina raciocínio lógico com ações práticas para produzir uma saída mais precisa e contextualizada.

## O que é ReAct?

ReAct, que significa "Reasoning and Acting" (Raciocínio e Ação), é uma técnica usada em modelos de linguagem para melhorar a capacidade de realizar tarefas que envolvem múltiplos passos de raciocínio lógico seguidos por uma ação correspondente. No contexto da geração de código, isso significa que o modelo primeiro explica a lógica ou o raciocínio por trás da solução antes de gerar o código.

## Funcionamento do Projeto

Neste projeto, implementamos uma função `react_model` que simula o comportamento de um modelo de linguagem utilizando ReAct. A função recebe um `prompt` como entrada, que descreve uma tarefa (neste caso, a geração de código para calcular o fatorial de um número). A função então:

1. **Raciocínio:** Gera uma explicação detalhada do raciocínio por trás da solução do problema.
2. **Ação:** Com base no raciocínio, gera o código Python correspondente que realiza a tarefa descrita.

### Para testar basta instalar a biblioteca do OpenAI

```python
pip install openai
