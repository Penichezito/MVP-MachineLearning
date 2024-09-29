import PropTypes from 'prop-types';
import'./ItemsTable.css';

const ItemsTable = ({ items, fetchedItems, deleteItem }) => {
  const combinedItems = [...fetchedItems, ...items];

  return (
    <section className="items">
      <table id="myTable">
        <thead>
          <tr>
            <th>Manufacturer</th>
            <th>Category</th>
            <th>Screen</th>
            <th>GPU</th>
            <th>OS</th>
            <th>CPU_Core</th>
            <th>Screen_Size_Inch</th>
            <th>CPU_frequency</th>
            <th>RAM_GB</th>
            <th>Storage_GB_SSD</th>
            <th>Weight_kg</th>
            <th>Price</th>
            <th><img src="https://cdn-icons-png.flaticon.com/512/126/126468.png" width="15" height="15" alt="delete" /></th>
          </tr>
        </thead>
        <tbody>
          {combinedItems.map((item, index) => (
            <tr key={index}>
              <td>{item.manufacturer}</td>
              <td>{item.category}</td>
              <td>{item.screen}</td>
              <td>{item.gpu}</td>
              <td>{item.os}</td>
              <td>{item.cpu_core}</td>
              <td>{item.screen_size_inch}</td>
              <td>{item.cpu_frequency}</td>
              <td>{item.ram_gb}</td>
              <td>{item.storage_gb_ssd}</td>
              <td>{item.weight_kg}</td>
              <td>{item.price}</td>  
              <td>Recomendação</td>
              <td><img src="https://cdn-icons-png.flaticon.com/512/126/126468.png" width="15" height="15" alt="delete" onClick={() => deleteItem(index)} /></td>
            </tr>
          ))}
        </tbody>
      </table>
    </section>
  );
};

ItemsTable.propTypes = {
  items: PropTypes.array.isRequired,
  fetchedItems: PropTypes.array.isRequired,
  deleteItem: PropTypes.func.isRequired,
};

export default ItemsTable