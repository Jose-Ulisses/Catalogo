document.addEventListener("DOMContentLoaded", () => {
    const produtosContainer = document.getElementById("produtos-container");
  
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