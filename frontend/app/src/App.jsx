import './App.css';
import { useState, useEffect } from 'react';
import NewItemForm from './components/NewItemForm/NewItemForm';
import ItemsTable from './components/ItemsTable/ItemsTable';

const App = () => {
  const [newItem, setNewItem] = useState({
    manufacturer: '',
    category: '',
    screen: '',
    gpu: '',
    os: '',
    cpu_core: '',
    screen_size_inch: '',
    cpu_frequency: '',
    ram_gb: '',
    storage_gb_ssd: '',
    weight: '',
    price: '',
  });
  
  const [items, setItems] = useState([]);
  const [fetchedItems, setFetchedItems] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch('http://127.0.0.1:5000/laptops');
        const data = await response.json();
        setFetchedItems(data);
      } catch (error) {
        console.error('Erro ao buscar dados:', error);
      }
    };

    fetchData();
  }, []);

  const handleChange = (e) => {
    const { id, value } = e.target;
    setNewItem(prevState => ({ ...prevState, [id]: value }));
  };

  const addItem = () => {
    setItems([...items, newItem]);
    setNewItem({
      manufacturer: '',
      category: '',
      screen: '',
      gpu: '',
      os: '',
      cpu_core: '',
      screen_size_inch: '',
      cpu_frequency: '',
      ram_gb: '',
      storage_gb_ssd: '',
      weight: '',
      price: '',
    });
  };

  const deleteItem = (index) => {
    setItems(items.filter((_item, i) => i !== index));
  };

  return (
    <>
      <div>
        <h1>MVP Laptop Recomendations</h1>
        <p>Para isso, basta preencher os campos abaixo com os dados e clicar em Recomendar.</p>
      </div>

      <section className='container'>
        <div className='input-item'>
          <NewItemForm newItem={newItem} handleChange={handleChange} addItem={addItem} />
        </div>
        <div className='items-table'>
            <ItemsTable items={items} fetchedItems={fetchedItems} deleteItem={deleteItem} />     
        </div>
      </section>  
    </>
  )
}

export default App
