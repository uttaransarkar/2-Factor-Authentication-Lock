import React,{useRef,useState,useEffect} from 'react';


function CameraInput(){
    const videoRef = useRef(null);
    const photoRef = useRef(null);
    const [hasPhoto,setHasPhoto] = useState(false);

    const getVideo = () => {
        navigator.mediaDevices.getUserMedia({ video: { width: 1280, height: 600} })
        .then(stream => {
            let video = videoRef.current;
            video.srcObject = stream;
            video.play();
        })
        .catch(err => {
            console.error(err);
        })
    }

    const takePhoto = () => {
        const width = 1280;
        const height = 520;

        let video = videoRef.current;
        let photo = photoRef.current;

        let ctx = photo.getContext('2d');
        ctx.drawImage(video,100,100,width,height,0,0,width/4, height/4);
        setHasPhoto(true);
    }

    const closePhoto = () => {
        let photo = photoRef.current;
        let ctx = photo.getContext('2d');

        ctx.clearRect(0,0,photo.width,photo.height);
        setHasPhoto(false);
    }

    useEffect(() => {
        getVideo()
    },[videoRef])

    return (
        <div>
            <div className="camera">
                <video ref={videoRef}></video>
                <button onClick={takePhoto}>SNAP</button>
            </div>
            <div className={'result '+(hasPhoto ? 'hasPhoto' : '')}>
                <canvas ref={photoRef}></canvas>
                <button onClick={closePhoto}>CLOSE</button>
            </div>
            
        </div>
        )
}
export default CameraInput