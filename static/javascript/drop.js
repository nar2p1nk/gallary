document.querySelectorAll('.input').forEach(inputElement =>{
  const dropZoneElement = inputElement.closest('.drop-zone');

  dropZoneElement.addEventListener('click', listener =>{
    inputElement.click();
    console.log('clicked')
  })

  inputElement.addEventListener('change', listener =>{
    
    if(inputElement.files.length){
      updateThumb(dropZoneElement, inputElement.files[0])
    }

  })


  dropZoneElement.addEventListener('dragover', e =>{
    e.preventDefault()
    dropZoneElement.classList.add('drop-zone--over')
    console.log('dragover')
  });

  ['dragleave','dragend'].forEach(type =>{
    dropZoneElement.addEventListener(type,e =>{
      dropZoneElement.classList.remove('drop-zone--over')
    })
  });

  dropZoneElement.addEventListener('drop', e =>{
    e.preventDefault()
    console.log('drop')
    

    if(e.dataTransfer.files.length){
      inputElement = e.dataTransfer.files;
      updateThumb(dropZoneElement, e.dataTransfer.files[0]);
    }

    dropZoneElement.classList.remove('drop-zone--over');


  })

});

/**
 * Updates the thumbnail on a drop zone element.
 *
 *@param {HTMLElement} dropZoneElement
 *@param {File} file
 */


function updateThumb(dropZoneElement,file){
  let thumbElement = dropZoneElement.querySelector('.thumbnail');

  // first time -- remove the prompt
  if (dropZoneElement.querySelector('.prompt')){
      dropZoneElement.querySelector('.prompt').remove();
  }
  // first time -- if there are no thumbnail element, this will create it
  if (!thumbElement){
    thumbElement = document.createElement('div');
    thumbElement.classList.add('thumbnail')
    dropZoneElement.appendChild(thumbElement)
  }

  thumbElement.dataset.label = file.name
  
  // show thumbnail for image file
  if(file.type.startsWith('image/')){
    const reader = new FileReader();

    reader.readAsDataURL(file);
    reader.onload = () =>{
      thumbElement.style.backgroundImage = `url('${reader.result}')`;
    }
  }
  else{
    thumbElement.style.backgroundImage = null
  }
}
console.log('ass')
