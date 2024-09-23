import { useState } from "react"
import "./TextField.css"

const TextField = (props) => {

    const ModifyPlaceholder = `${props.placeholder} ...`
    // let value = ""
    const[value, setValue] = useState("")

    const whenTyped = (event) => {
        setValue (event.target.value)
        console.log(value)
    }

    return(
        <div className="text-field">
            <label>{props.label}</label>
            <input value={props.value} onChange={whenTyped} required={props.mandatory} placeholder={ModifyPlaceholder}/>
        </div>
    )
}

export default TextField