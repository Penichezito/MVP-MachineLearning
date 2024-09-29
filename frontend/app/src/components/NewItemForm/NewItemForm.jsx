import './NewItemForm.css'
import PropTypes from 'prop-types';

const NewItemForm = ({ newItem, handleChange, addItem }) => {
  return (
    <section className="newItem">
      <input type="text" id="manufacturer" placeholder="Modelo/Marca do Notebook" value={newItem.manufacturer} onChange={handleChange} />
      <input type="text" id="category" placeholder="Categoria Notebook" value={newItem.category} onChange={handleChange} />
      <input type="text" id="screen" placeholder="Tipo de Tela" value={newItem.screen} onChange={handleChange} />
      <input type="text" id="gpu" placeholder="GPU" value={newItem.gpu} onChange={handleChange} />
      <input type="text" id="os" placeholder="Sistema Operacional" value={newItem.os} onChange={handleChange} />
      <input type="text" id="cpu_core" placeholder="CPU Core" value={newItem.cpu_core} onChange={handleChange} />
      <input type="text" id="screen_size_inch" placeholder="Polegadas da Tela" value={newItem.screen_size_inch} onChange={handleChange} />
      <input type="text" id="cpu_frequency" placeholder="Frequencia CPU" value={newItem.cpu_frequency} onChange={handleChange} />
      <input type="text" id="ram_gb" placeholder="RAM GB" value={newItem.ram_gb} onChange={handleChange} />
      <input type="text" id="storage_gb_ssd" placeholder="armazenamento ssd" value={newItem.storage_gb_ssd} onChange={handleChange} />
      <input type="text" id="weight_kg" placeholder="peso kg" value={newItem.weight_kg} onChange={handleChange} />
      <input type="text" id="price" placeholder="preço" value={newItem.price} onChange={handleChange} />
      <button onClick={addItem} className="addBtn">Recomendar</button>
    </section>
  );
};

NewItemForm.propTypes = {
  newItem: PropTypes.shape({
    manufacturer: PropTypes.string,
    category: PropTypes.string,
    screen: PropTypes.string,
    gpu: PropTypes.string,
    os: PropTypes.string,
    cpu_core: PropTypes.string,
    screen_size_inch: PropTypes.string,
    cpu_frequency: PropTypes.string,
    ram_gb: PropTypes.string,
    storage_gb_ssd: PropTypes.string,
    weight_kg: PropTypes.string,
    price: PropTypes.string,
  }).isRequired,
  handleChange: PropTypes.func.isRequired,
  addItem: PropTypes.func.isRequired,
};

export default NewItemForm