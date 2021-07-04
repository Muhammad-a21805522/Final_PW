 function addT(){
        let text = document.getElementById('tecnicas1')
        text.innerHTML='Django: Integrámos a linguagem django na segunda e terceira parte do nosso projeto e para tal utilizámos conceitos como: models, views, linguagem template e urls.' +
            'Model: Um conjunto de ferramentas que tornam fácil o trabalho com as bases de dados.' +
            ' Template: Um sistema de templates adequado para designers.' +
            ' Views: Ligação entre os dados do Model e os Templates, está por detrás das lógicas de negócio da app.' +
            ' Nos views, basicamente cada função é responsável por dar o return de uma view, que é uma resposta ao pedido de uma rota.' +
            ' Cada url mapeia uma função que retorna uma resposta e o HttpResponse retorna uma string ao cliente.' +
            ' A linguagem Template especifica o aspeto da página web, permite renderizar um template HTML com conteúdos da primeira parte do projeto como context e utiliza a herança de ficheiros de modo a minimizar a escrita de código.' +
            ' Utilizámos o csrf-token para a proteção dos dados dos formulários contra hackers e ataques informáticos, também utilizamos o ciclo for para o loop da lista de contactos e comentários.' +
            ' Nos models.py modificamos a classe Quizz interligada com os Contactos através da Foreign Key.'+
            'Javascript: Utilizámos esta linguagem de programação na última parte do projeto de modo a termos uma programação orientada a eventos. Utilizámos vários conceitos como: ' +
            ' OnClick: O utilizador clica no botão ou em outro elemento.' +
            ' OnMouseover: O utilizador move o rato sobre um elemento HTML.' +
            ' Com estes eventos manipulamos o DOM, alterando elementos HTMl existentes, como o ElementById, innerHTML e mudar a cor do texto através do style.color'
    }
