import Roupa from './Roupa.js';

document.addEventListener("DOMContentLoaded", () => {
    const produtosContainer = document.getElementById("produtos-container");
  
    // Função assíncrona para buscar e digerir os dados
    const roupas = async () => {
      try {
        const response = await fetch("https://nossoapi.com/roupas", );
        
        if (!response.ok) {
          throw new Error(`Erro na requisição: ${response.status}`);
        }

        const data = await response.json();

        // Mapeia cada item do JSON para uma instância da classe Roupa
        const roupasList = data.map(item => new Roupa(
          item.path,
          item.name,
          item.gender,
          item.size,
          item.color,
          item.type,
          item.season,
          item.price
        ));

        console.log(roupasList);
        return roupasList;

      } catch (error) {
        console.error("Erro ao buscar roupas:", error);
      }
    };

    const totalProdutos = 12;
    const produtos = [];

    for(let i = 1; i <= totalProdutos; i++){
        produtos.push({
            nome: `produto ${i}`,
            imagem: `../../imagens/casacos_jaquetas_masc/produto${i}.jpg`,
            preco: "R$ 199,90",
        });
    }

    produtos.forEach(produto => {
      const card = document.createElement("div");
      card.classList.add("card");
  
      card.innerHTML = `
        <img src="${produto.imagem}" alt="${produto.nome}">
        <h3>${produto.nome}</h3>
        <p>${produto.preco}</p>
      `;
  
      produtosContainer.appendChild(card);
    });
  });
