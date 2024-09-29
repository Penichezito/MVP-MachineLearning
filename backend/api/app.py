from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote
from sklearn.preprocessing import OneHotEncoder
from sqlalchemy.exc import IntegrityError

from model import *
from logger import logger
from schemas import *
from flask_cors import CORS


# Instanciando o objeto OpenAPI
info = Info(title="ML Laptops Recomendation", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# Definindo tags para agrupamento das rotas
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
laptop_tag = Tag(name="Laptop", description="Adição, visualização, remoção e predição de modelos de laptops para recomendação")


# Rota home
@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')


# Rota de listagem dos laptops
@app.get('/laptops', tags=[laptop_tag],
         responses={"200": LaptopViewSchema, "404": ErrorSchema})
def get_laptops():
    """Lista todos os laptops cadastrados na base
    Args:
       none
        
    Returns:
        list: lista de laptops cadastrados na base
    """
    logger.debug("Coletando dados sobre todos os laptops")
    # Criando conexão com a base
    session = Session()
    # Buscando todos os laptops
    laptops = session.query(Laptop).all()
    
    if not laptops:
            # Se não houver laptops
        return {"laptops": []}, 200
    else:
        logger.debug(f"%d laptops econtrados" % len(laptops))
        print(laptops)
        return presentation_laptops(laptops), 200


# Rota de adição de laptops
@app.post('/laptop', tags=[laptop_tag],
          responses={"200": LaptopViewSchema, "400": ErrorSchema, "409": ErrorSchema})
def predict(form: LaptopSchema):
    """Adiciona um novo laptop à base de dados
    Retorna uma representação dos laptops e recomendações associados.
    
    Args:
        Manufacturer: marca do laptop
            category: categoria a que pertece o laptop
            screen:top de tela
            gpu: placa de vídeo (dedicada ou externa)
            os: pressão sanguínea
            cpu_core: espessura da pele
            screen_size_inch: tamanho da tela
            cpu_frequency: frequencia de velocidade de processamento da cpu
            ram_gb: quantidade de memoria ram
            storage_gb_ssd: armazenamento em gb do laptop
            weight_kg: peso do laptop
            price:preço do laptop
            date_insertion: data de quando o laptop foi inserido à base
    Returns:
        dict: representação do laptop com recomendação
    """
    # TODO: Instanciar classes

    # Recuperando os dados do formulário
    manufacturer = form.manufacturer
    category = form.category
    screen = form.screen
    gpu = form.gpu
    os = form.os
    cpu_core = form.cpu_core
    screen_size_inch = form.screen_size_inch
    cpu_frequency = form.cpu_core
    ram_gb = form.ram_gb
    storage_gb = form.storage_gb
    weight_kg = form.weight_kg
    price = form.price
        
   # Instancia a classe Model
    model_instance = Model()

    # Caminho do modelo
    model_path = './MachineLearning/pipelines/pipeline.pkl'

    # Chame o método load_model com o caminho do modelo
    model_instance.load_model(model_path)

    # Preparando os dados para o modelo com o PreProcessor
    preprocessor = PreProcessor() 
    x_input_prepared = Pipeline.load_data(model_path) # Adapte o nome do método se necessário

    # Realizando a predição
    encoder = OneHotEncoder(sparse_output=False, handle_unknown='ignore')
    x_input_encoded = encoder.fit_transform(x_input_prepared)
    recomendation = int(Model.predict(x_input_encoded)[0])
    
    laptop = Laptop(       
    manufacturer=manufacturer,
    category=category,
    screen=screen,
    gpu=gpu,
    os=os,
    cpu_core=cpu_core,
    screen_size_inch=screen_size_inch,
    cpu_frequency=cpu_frequency,
    ram_gb=ram_gb,
    storage_gb=storage_gb,
    weight_kg=weight_kg,
    price=price,
    recomendation=recomendation
    )
    logger.debug(f"Adicionando produto da marca/modelo: '{laptop.manufacturer}'")
    
    try:
        # Criando conexão com a base
        session = Session()
        
        # Checando se laptop já existe na base
        if session.query(Laptop).filter(Laptop.manufacturer == form.manufacturer).first():
            error_msg = "Laptop já existente na base :/"
            logger.warning(f"Erro ao adicionar laptop '{laptop.manufacturer}', {error_msg}")
            return {"message": error_msg}, 409
        
        # Adicionando laptop
        session.add(laptop)
        # Efetivando o comando de adição
        session.commit()
        # Concluindo a transação
        logger.debug(f"Adicionado laptop de nome: '{laptop.manufacturer}'")
        return presentation_laptop(laptop), 200
    
    # Caso ocorra algum erro na adição
    except Exception as e:
        error_msg = "Não foi possível salvar novo item :/"
        logger.warning(f"Erro ao adicionar laptop '{laptop.manufacturer}', {error_msg}")
        return {"message": error_msg}, 400
    

# Métodos baseados em nome
# Rota de busca de laptop por nome
@app.get('/laptop', tags=[laptop_tag],
         responses={"200": LaptopViewSchema, "404": ErrorSchema})
def get_laptop(query: LaptopSearchSchema):    
    """Faz a busca por um laptop cadastrado na base a partir do nome

    Args:
        nome (str): nome do laptop
        
    Returns:
        dict: representação de recomendação do produto
    """
    
    laptop_manufacturer = query.manufacturer
    logger.debug(f"Coletando dados sobre produto #{laptop_manufacturer}")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    laptop = session.query(Laptop).filter(Laptop.manufacturer == laptop_manufacturer).first()
    
    if not laptop:
        # se o paciente não foi encontrado
        error_msg = f"Laptop {laptop_manufacturer} não encontrado na base :/"
        logger.warning(f"Erro ao buscar produto '{laptop_manufacturer}', {error_msg}")
        return {"mesage": error_msg}, 404
    else:
        logger.debug(f"Laptop econtrado: '{laptop.manufacturer}'")
        # retorna a representação do paciente
        return presentation_laptop(laptop), 200
   
    
# Rota de remoção de laptop pela marca
@app.delete('/laptop', tags=[laptop_tag],
            responses={"200": LaptopViewSchema, "404": ErrorSchema})
def delete_laptop(query: LaptopSearchSchema):
    """Remove um laptop cadastrado na base a partir da marca

    Args:
        manufacturer (str): marca do laptop
        
    Returns:
        msg: Mensagem de sucesso ou erro
    """
    
    laptop_manufacturer = unquote(query.manufacturer)
    logger.debug(f"Deletando dados sobre o produto #{laptop_manufacturer}")
    
    # Criando conexão com a base
    session = Session()
    
    # Buscando laptop
    laptop = session.query(Laptop).filter(Laptop.id == laptop_manufacturer).first()
    
    if not laptop:
        error_msg = "Laptop não encontrado na base :/"
        logger.warning(f"Erro ao deletar laptop '{laptop_manufacturer}', {error_msg}")
        return {"message": error_msg}, 404
    else:
        session.delete(laptop)
        session.commit()
        logger.debug(f"Deletado laptop #{laptop_manufacturer}")
        return {"message": f"Laptop {laptop_manufacturer} removido com sucesso!"}, 200
    
if __name__ == '__main__':
    app.run(debug=True)