from shiny import App, ui, reactive, render
import requests
import tempfile
import io

app_ui = ui.page_sidebar(
	ui.sidebar(
		ui.input_radio_buttons(
			id="canal",
			label="Canal:",
			choices={
				"01": "1 Azul",
				"02": "2 Vermelho",
				"03": "3 Veggie",
				"04": "4 Cirrus",
				"05": "5 Neve/Gelo",
				"06": "6 Part. Nuvem",
				"07": "7 IR Onda curta",
				"08": "8 WV altos níveis",
				"09": "9 WV médios níveis",
				"10": "10 WV baixos níveis",
				"11": "11 Fase da nuvem IR",
				"12": "12 Ozônio",
				"13": "13 IR Limpo",
				"14": "14 IR Onda longa",
				"15": "15 IR Sujo",
				"16": "16 CO2",
			},
			selected="13"
		),
		ui.download_link("baixar_manual", "Baixe o guia rápido GOES-16/19"),
	),
	ui.h2("Imagens mais recentes GOES-19"),
	ui.row(ui.column(6,
			ui.output_image("canal_img"),
		),
	ui.column(6,
			ui.h6("Este é um app Shiny em Python com fins demonstrativos."),
			ui.h6("Este app funciona sob o mesmo serviço de um app Shiny em R."),
			ui.h6("Imagens: STAR-NESDIS-NOAA"),
		)
	),
)

def server(input, output, session):
	@output
	@render.image
	def canal_img():
		canal = input.canal()
		url = f"https://cdn.star.nesdis.noaa.gov/GOES19/ABI/FD/{canal}/1808x1808.jpg"
		resposta = requests.get(url)
		temporario = tempfile.NamedTemporaryFile(suffix=".jpg", delete=False)
		temporario.write(resposta.content)
		temporario.flush()
		return {
			"src": temporario.name,
			"alt": f"Imagem do Canal {canal}",
			"style": "width: 100%"
		}

	@render.download
	def baixar_manual():
		return "guia_rapido_goes.pdf"

app = App(app_ui, server)

