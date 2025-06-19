A aplicação é simples e já foi publicada (hospedada) em um Shiny Server, junto a aplicações Shiny em R.

A interface é uma barra lateral (sidebar) com 16 radio buttons para escolher a imagem que será exibida, e mais abaixo um link de download de um arquivo pdf.
O painel principal é dividido meio a meio entre a imagem e um texto.

A seção do servidor mostra qual URL é usada para buscar a imagem [https://www.star.nesdis.noaa.gov/GOES/fulldisk.php?sat=G19] e como a escolha do radio button é usada pelo servidor.
Vê-se ainda como a imagem buscada é trazida para um arquivo temporário e utilizada no back-end.

Esse produto tem fins demonstrativos para divulgação de aplicações web Shiny em Python, e não se propõe a embasar tomada de decisão em qualquer organização.
