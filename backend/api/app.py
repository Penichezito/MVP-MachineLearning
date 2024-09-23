from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

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
paciente_tag = Tag(name="Laptop", description="Adição, visualização, remoção e predição de modelos de laptops para recomendação")


# Rota home
@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')


# Rota de listagem dos laptops
@app.get('/laptops', tags=[laptops_tag],
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
    
    if not Laptops:
            # Se não houver laptops
        return {"laptops": []}, 200
    else:
        logger.debug(f"%d laptops econtrados" % len(laptops))
        print(laptops)
        return presentation_laptops(laptops), 200


# Rota de adição de laptops
@app.post('/laptop', tags=[paciente_tag],
          responses={"200": LaptopViewSchema, "400": ErrorSchema, "409": ErrorSchema})
def predict(form: LaptopSchema):
    """Adiciona um novo paciente à base de dados
    Retorna uma representação dos pacientes e diagnósticos associados.
    
    Args:
        manufacterer (str): marca do laptop
        category (int): número de vezes que engravidou: Pregnancies
         (int): concentração de glicose no plasma: Glucose
        pres (int): pressão diastólica (mm Hg): BloodPressure
        skin (int): espessura da dobra cutânea do tríceps (mm): SkinThickness
        test (int): insulina sérica de 2 horas (mu U/ml): Insulin
        mass (float): índice de massa corporal (peso em kg/(altura em m)^2): BMI
        pedi (float): função pedigree de diabetes: DiabetesPedigreeFunction
        age (int): idade (anos): Age
        
    Returns:
        dict: representação do paciente e diagnóstico associado
    """
    # TODO: Instanciar classes

    # Recuperando os dados do formulário
    name = form.name
    preg = form.preg
    plas = form.plas
    pres = form.pres
    skin = form.skin
    test = form.test
    mass = form.mass
    pedi = form.pedi
    age = form.age
        
    # Preparando os dados para o modelo
    X_input = PreProcessor.preparar_form(form)
    # Carregando modelo
    model_path = './MachineLearning/pipelines/rf_diabetes_pipeline.pkl'
    # modelo = Model.carrega_modelo(ml_path)
    modelo = Pipeline.load_pipeline(model_path)
    # Realizando a predição
    recomendation = int(Model.preditor(modelo, X_input)[0])
    
    laptop = Laptop(
    
    id: int = 1
    Manufacterer=
    Category= 
    Screen=
    GPU=
    os=
    CPU_core=
    Screen_Size_inch=
    CPU_Frequency=
    RAM_GB=
    Storage_GB_SSD=
    Price=
    Recomendation=
    )
    logger.debug(f"Adicionando produto de nome: '{laptop.manufacturer}'")
    
    try:
        # Criando conexão com a base
        session = Session()
        
        # Checando se paciente já existe na base
        if session.query(Paciente).filter(Paciente.name == form.name).first():
            error_msg = "Paciente já existente na base :/"
            logger.warning(f"Erro ao adicionar paciente '{paciente.name}', {error_msg}")
            return {"message": error_msg}, 409
        
        # Adicionando paciente
        session.add(paciente)
        # Efetivando o comando de adição
        session.commit()
        # Concluindo a transação
        logger.debug(f"Adicionado paciente de nome: '{paciente.name}'")
        return apresenta_paciente(paciente), 200
    
    # Caso ocorra algum erro na adição
    except Exception as e:
        error_msg = "Não foi possível salvar novo item :/"
        logger.warning(f"Erro ao adicionar paciente '{paciente.name}', {error_msg}")
        return {"message": error_msg}, 400
    

# Métodos baseados em nome
# Rota de busca de paciente por nome
@app.get('/paciente', tags=[paciente_tag],
         responses={"200": PacienteViewSchema, "404": ErrorSchema})
def get_paciente(query: PacienteBuscaSchema):    
    """Faz a busca por um paciente cadastrado na base a partir do nome

    Args:
        nome (str): nome do paciente
        
    Returns:
        dict: representação do paciente e diagnóstico associado
    """
    
    paciente_nome = query.name
    logger.debug(f"Coletando dados sobre produto #{paciente_nome}")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    paciente = session.query(Paciente).filter(Paciente.name == paciente_nome).first()
    
    if not paciente:
        # se o paciente não foi encontrado
        error_msg = f"Paciente {paciente_nome} não encontrado na base :/"
        logger.warning(f"Erro ao buscar produto '{paciente_nome}', {error_msg}")
        return {"mesage": error_msg}, 404
    else:
        logger.debug(f"Paciente econtrado: '{paciente.name}'")
        # retorna a representação do paciente
        return apresenta_paciente(paciente), 200
   
    
# Rota de remoção de paciente por nome
@app.delete('/paciente', tags=[paciente_tag],
            responses={"200": PacienteViewSchema, "404": ErrorSchema})
def delete_paciente(query: PacienteBuscaSchema):
    """Remove um laptop cadastrado na base a partir da marca

    Args:
        nome (str): nome do paciente
        
    Returns:
        msg: Mensagem de sucesso ou erro
    """
    
    paciente_nome = unquote(query.name)
    logger.debug(f"Deletando dados sobre paciente #{paciente_nome}")
    
    # Criando conexão com a base
    session = Session()
    
    # Buscando paciente
    paciente = session.query(Laptop).filter(Laptop.manufacturer == laptop_manufacturer).first()
    
    if not paciente:
        error_msg = "Laptop não encontrado na base :/"
        logger.warning(f"Erro ao deletar laptop '{paciente_nome}', {error_msg}")
        return {"message": error_msg}, 404
    else:
        session.delete(laptop)
        session.commit()
        logger.debug(f"Deletado paciente #{laptop_manufacturer}")
        return {"message": f"Laptop {laptop_manufacturer} removido com sucesso!"}, 200
    
if __name__ == '__main__':
    app.run(debug=True)