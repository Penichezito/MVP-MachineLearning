import "./Form.css"
import TextField from "../TextField"
import DropdownList from "../DropdownList"
import Button from "../Button"
import { useState } from "react"

const Form = () => {

    const headerVariables =[
        "Programação",
        "Front-End",
        "Data Science",
        "Devops",
        "UX e Design",
        "Mobile",
        "Inovação"
    ]

    const [nome, setNome] = useState("")
    const [cargo, setCargo] = useState("")
    const [imagem, setImagem] = useState("")
   

    const whenSaving = (event) => {
        event.preventDefault()
        console.log("Formulário submetido com sucesso")
    }

    return (
        <section className="form">
            <form onSubmit={whenSaving}>
                <h2>Preencha os Dados para criar o card do colaborador</h2>
                <TextField 
                    mandatory={true} 
                    label="Nome" 
                    placeholder="Digite seu nome">  
                    value = {nome}
                    whenChanged={value => setNome(value)}
                </TextField>
                <TextField 
                    mandatory={true} 
                    label="Cargo" 
                    placeholder="Digite seu cargo">
                    value={cargo}
                    whenChanged={value => setCargo(value)}
                </TextField>
                <TextField 
                    label="Imagem" 
                    placeholder="Digite o endereço da imagem">
                         value={imagem}
                         whenChanged={value => setImagem(value)}
                </TextField>
                <DropdownList mandatory={true} label="Times" itens={teams}></DropdownList>
                <Button>Criar Card</Button>
            </form>
        </section>
    )
}

export default Form