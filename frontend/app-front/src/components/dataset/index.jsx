// import Form, { useState, useEffect } from 'react';

// function LaptopList() {
//   const [laptops, setlaptops] = useState([]);

//   useEffect(() => {
//     const fetchLaptops = async () => {
//       try {
//         const response = await fetch('http://127.0.0.1:5000/laptops');
//         const data = await response.json();
//         setLaptops(data.laptops || []); // Handle potential empty data
//       } catch (error) {
//         console.error('Error fetching laptops:', error);
//       }
//     };

//     fetchLaptops();
//   }, []);

//   const handleDelete = async (manufacter) => {
//     try {
//       const response = await fetch(`http://127.0.0.1:5000/laptop?name=${manufacter}`, {
//         method: 'DELETE',
//       });

//       if (response.ok) {
//         setlaptops(laptops.filter((laptop) => laptop.manufacter !== manufacter));
//       } else {
//         console.error('Error deleting laptop:', await response.text());
//       }
//     } catch (error) {
//       console.error('Error deleting laptop:', error);
//     }
//   };

//   const handleNewLaptop = async (formData) => {
//     try {
//       const response = await fetch('http://127.0.0.1:5000/laptop', {
//         method: 'POST',
//         body: JSON.stringify(formData),
//         headers: { 'Content-Type': 'application/json' },
//       });

//       if (response.ok) {
//         const newLaptop = await response.json();
//         setLaptops([...laptops, newLaptop]); // Add new laptop to state
//         // Clear form fields after successful addition (optional)
//       } else {
//         console.error('Error adding laptop:', await response.text());
//       }
//     } catch (error) {
//       console.error('Error adding laptop:', error);
//     }
//   };

//   return (
//     <div>
//       <h1>Lista de Notebooks</h1>
//       <table>
//         <thead>
//           <tr>
//             <th>Manufacter</th>
//             <th>Category</th>
//             <th>Screen</th>
//             <th>GPU</th>
//             <th>os</th>
//             <th>CPU_core</th>
//             <th>Screen_Size_inch</th>
//             <th>CPU_Frequency</th>
//             <th>RAM_GB</th>
//             <th>Storage_GB_SSD</th>
//             <th>Price</th>
//             <th>Recomendation</th>
//           </tr>
//         </thead>
//         <tbody>
//           {laptops.map((laptop) => (
//             <tr key={laptop.manufacter}>
//               <td>{laptop.manufacter}</td>
//               <td>{laptop.Category}</td>
//               <td>{laptop.Screen}</td>
//               <td>{laptop.GPU}</td>
//               <td>{laptop.os}</td>
//               <td>{laptop.CPU_core}</td>
//               <td>{laptop.Screen_Size_inch}</td>
//               <td>{laptop.CPU_Frequency}</td>
//               <td>{laptop.RAM_GB}</td>
//               <td>{laptop.Storage_GB_SSD}</td>
//               <td>{laptop.Price}</td>
//               <td>{laptop.Recomendation}</td>
//               <td>
//                 <button onClick={() => handleDelete(laptop.manufacter)}>
//                   Excluir
//                 </button>
//               </td>
//             </tr>
//           ))}
//         </tbody>
//       </table>
//       <form onSubmit={(e) => e.preventDefault()}>
//         <h2>Adicionar Informações</h2>
//         <label>
//           Nome:
//           <input type="text" id="newInput" required />
//         </label>
//         {/* Add other input fields for preg, plas, etc. */}
//         <button type="submit" onClick={() => handleNewLaptop( /* form data */ )}>
//           Adicionar
//         </button>
//       </form>
//     </div>
//   );
// }

// export default LaptopList;