import React, {useState} from "react";
import Modal from 'react-modal';
import '../modal.css'
function LoadingModal() {

    const [isOpen, setIsOpen] = useState(true);

    const openModal = () => setIsOpen(true);
    const closeModal = () => setIsOpen(false);
    return (
        <Modal
              id = "loading_modal"
              isOpen={isOpen}
              onRequestClose={closeModal} style={{overlay: {
                display: 'flex',
                justifyContent: 'center',
                alignContent: 'center',
                top: 0,
                left: 0,
                right: 0,
                bottom: 0,
                backgroundColor: 'rgba(255, 255, 255, 0.75)'
              },
              content: {
                position: 'absolute',
                fontFamily: "'Gowun Batang', serif",
                margin :'auto',
                border: '1px solid #ccc',
                background: 'rgba(255, 255, 255, 0)',
                outline: 'none',
                border: 'none',
                bottom: 0,
                width:700,
                height:700,
                padding: '20px'
              }}}>
                <div className="overlay-box" >
                  <p>잠시만 기다려주세요</p>
                </div>
              
            </Modal>
    )
}
export default LoadingModal;
