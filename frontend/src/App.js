import React, { Component } from 'react';
import axios from 'axios';
class App extends Component {
    state = {
    menus: []
    };
    
    componentDidMount() {
    this.getMenus();
    }
    
    getMenus() {
    axios
        .get('http://127.0.0.1:8000/api/')
        .then(res => {
        this.setState({ menus: res.data });
    })
        .catch(err => {
            console.log(err);
    });
    }
  render() {
    return (
      <div>
      {this.state.menus.map(item => 
      <div key={item.order}>
      <h1>{item.name}</h1>
      <p>{item.additional_text}</p>
      {item.menucategory.map((c,i)=>(
        <div key={i.order}>
          <h1>{c.name}</h1>
          <p>{c.description}</p>
          {c.menuitem.map((m,n)=>(
            <div key={n.order}>
            <h1>{m.name} = {m.price} Euro</h1>
            <p>{m.description}</p>
            </div>
          ))}
        </div>
      ))}
        </div>)}
      </div>
      );
    }
}
      export default App;