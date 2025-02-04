import customtkinter as ctk
from typing import Union

# Definindo cores que vou usar no projeto (achei essas na internet e gostei!)
COLORS = {
    'background': "#2C3E50",    # Azul escuro bonito pro fundo
    'text_light': "#ECF0F1",    # Cor clara para texto
    'text_dark': "#2C3E50",     # Cor escura para texto
    'button': "#3498DB",        # Azul mais vivo para botões
    'surface': "#E5E8E8",       # Cor suave para superfícies
    'accent': "#16A085",        # Verde água para destaques
    'disabled': "#95A5A6"       # Cinza para elementos desativados
}

class IMCCalculator:
    def __init__(self):
        # Configuração inicial da janela principal
        self.window = ctk.CTk()
        self.window.title("Minha Calculadora de IMC")
        self.window.geometry("460x540")
        self.window.configure(bg=COLORS['background'])
        
        self._create_frames()
        self._setup_ui()
    
    def _create_frames(self):
        # Criando os dois frames principais - um pra título e outro pro conteúdo
        self.upper_frame = ctk.CTkFrame(self.window, width=420, height=100, corner_radius=20, fg_color=COLORS['surface'])
        self.upper_frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)
        
        self.lower_frame = ctk.CTkFrame(self.window, width=420, height=420, corner_radius=20, fg_color=COLORS['surface'])
        self.lower_frame.grid(row=1, column=0, sticky="nsew", padx=20, pady=20)
    
    def _setup_ui(self):
        # Configuração do título
        self.title = ctk.CTkLabel(
            self.upper_frame,
            text="Calculadora de IMC",
            text_color=COLORS['accent'],
            font=("Arial", 30, 'bold'),
            corner_radius=20,
            anchor='center'
        )
        self.title.place(x=0, y=25, relwidth=1)
        
        # Campos de entrada com suas labels
        self._create_input_fields()
        
        # Área de resultado
        self._create_result_area()
        
        # Botão de calcular
        self._create_calculate_button()
    
    def _create_input_fields(self):
        # Campo de peso
        self.peso_label = ctk.CTkLabel(
            self.lower_frame,
            text="Digite seu peso (kg)",
            text_color=COLORS['text_dark'],
            font=("Arial", 14, 'bold')
        )
        self.peso_label.grid(row=0, column=0, sticky="nw", padx=15, pady=15)
        
        self.peso_entry = ctk.CTkEntry(
            self.lower_frame,
            width=200,
            font=("Arial", 14),
            corner_radius=12,
            justify='center'
        )
        self.peso_entry.grid(row=0, column=1, sticky="nsew", padx=15, pady=15)
        
        # Campo de altura
        self.altura_label = ctk.CTkLabel(
            self.lower_frame,
            text="Digite sua altura (m)",
            text_color=COLORS['text_dark'],
            font=("Arial", 14, 'bold')
        )
        self.altura_label.grid(row=1, column=0, sticky="nw", padx=15, pady=15)
        
        self.altura_entry = ctk.CTkEntry(
            self.lower_frame,
            width=200,
            font=("Arial", 14),
            corner_radius=12,
            justify='center'
        )
        self.altura_entry.grid(row=1, column=1, sticky="nsew", padx=15, pady=15)
    
    def _create_result_area(self):
        self.resultado_valor = ctk.CTkLabel(
            self.lower_frame,
            text="---",
            corner_radius=12,
            width=5,
            height=1,
            text_color=COLORS['accent'],
            font=("Arial", 32, 'bold'),
            anchor="center"
        )
        self.resultado_valor.grid(row=2, column=0, columnspan=2, padx=15, pady=30)
        
        self.resultado_texto = ctk.CTkLabel(
            self.lower_frame,
            text="",
            text_color=COLORS['text_dark'],
            font=("Arial", 16),
            anchor="center"
        )
        self.resultado_texto.grid(row=3, column=0, columnspan=2, padx=15, pady=15)
    
    def _create_calculate_button(self):
        self.calc_button = ctk.CTkButton(
            self.lower_frame,
            text="Calcular",
            command=self._calcular_imc,
            corner_radius=12,
            width=200,
            height=50,
            fg_color=COLORS['button'],
            hover_color="#2980B9",
            text_color=COLORS['text_light'],
            font=("Arial", 16, 'bold')
        )
        self.calc_button.grid(row=4, column=0, columnspan=2, padx=25, pady=15)
    
    def _validate_input(self, value: str) -> Union[float, None]:
        """Valida se o input pode ser convertido para float"""
        try:
            return float(value.replace(',', '.'))
        except ValueError:
            return None
    
    def _calcular_imc(self):
        """Calcula o IMC e atualiza a interface com o resultado"""
        peso = self._validate_input(self.peso_entry.get())
        altura = self._validate_input(self.altura_entry.get())
        
        if not peso or not altura:
            self.resultado_texto.configure(text="Por favor, digite valores válidos!")
            self.resultado_valor.configure(text="---")
            return
        
        # Calculando o IMC
        imc = peso / (altura ** 2)
        
        # Definindo a classificação
        if imc < 18.5:
            classificacao = "Abaixo do peso"
        elif imc < 24.9:
            classificacao = "Peso normal"
        elif imc < 29.9:
            classificacao = "Sobrepeso"
        else:
            classificacao = "Obesidade"
        
        # Atualizando a interface
        self.resultado_valor.configure(text=f"{imc:.2f}")
        self.resultado_texto.configure(text=classificacao)
    
    def run(self):
        """Inicia a aplicação"""
        self.window.mainloop()

# Criar e executar a aplicação
if __name__ == "__main__":
    app = IMCCalculator()
    app.run()