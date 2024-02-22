// import "./App.css";
// import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
// import { Navbar } from "./components/navbar";
// import { Shop } from "./pages/shop/shop";
// import { Contact } from "./pages/contact";
// import { Cart } from "./pages/cart/cart";
// import { ShopContextProvider } from "./context/shop-context";

// function App() {
//   return (
//     <div className="App">
//       <ShopContextProvider>
//         <Router>
//           <Navbar />
//           <Routes>
//             <Route path="/" element={<Shop />} />
//             <Route path="/contact" element={<Contact />} />
//             <Route path="/cart" element={<Cart />} />
//           </Routes>
//         </Router>
//       </ShopContextProvider>
//     </div>
//   );
// }

// export default App;
import "./App.css";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { Navbar } from "./components/navbar";
import { Shop } from "./pages/shop/shop";
import { Contact } from "./pages/contact";
import { Cart } from "./pages/cart/cart";
import { Login } from "./components/login";
import { Signup } from "./components/signup";
import { ShopContextProvider } from "./context/shop-context";

function App() {
  return (
    <div className="App">
      <ShopContextProvider>
        <Router>
          <Navbar />
          <Routes>
            <Route path="/" element={<Shop />} />
            <Route path="/contact" element={<Contact />} />
            <Route path="/cart" element={<Cart />} />
            <Route path="/login" element={<Login />} />
            <Route path="/signup" element={<Signup />} />
          </Routes>
        </Router>
      </ShopContextProvider>
    </div>
  );
}

export default App;
