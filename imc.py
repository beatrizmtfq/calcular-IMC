from flask import Flask, request, render_template


class CalculadoraIMC: 
    def __init__(self, nome, peso, altura, genero):
        self.nome = nome
        self.peso = peso
        self.altura = altura
        self.genero = genero


    def calcular_imc(self):
        imc = self.peso / (self.altura ** 2)
        return imc 
    
    def classificar_imc(self):
        imc = self.calcular_imc()
        if imc < 17:
            return "Muito abaixo do peso."
        elif 17 <= imc < 18.5:
            return "Abaixo do peso"
        elif 18.5 <= imc < 25:
            return "Peso normal"
        elif 25 <= imc < 30:
            return "Acima do peso"
        elif 30 <= imc < 35:
            return "Obesidade I"
        elif 35 <= imc < 40:
            return "Obesidade II"
        else:
            return "Obesidade III"


    def calcular_peso_ideal(self):
        if self.genero.lower() == "homem":
            return (72.7 * self.altura) - 58
        elif self.genero.lower() == "mulher":
            return (62.1 * self.altura) - 44.7
        else:
            return "Nenhum gênero reconhecido"
        

app = Flask(__name__)        

@app.route('/', methods = ['get', 'post'])
def calcular():
        if request.methods == 'post':
            nome = request.forms['nome']
            peso = float(request.forms['peso'])
            altura = float(request.forms['altura'])
            genero = request.forms ['genero']

            calculadora = CalculadoraIMC(nome, peso, altura, genero)
            imc = calculadora.calcular_imc()
            classificacao = calculadora.classificar_imc()
            peso_ideal = calculadora.calcular_peso_ideal()

            return render_template('./resultado.html', nome=nome, imc=imc, classificacao=classificacao, peso_ideal=peso_ideal)
            
            return render_template('formulario.html')

        if __name__ == '__name__':
            app.run(debug=True, host='127.0.0.1', port=8000)

                                   
            
    