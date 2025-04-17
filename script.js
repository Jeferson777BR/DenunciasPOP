document.getElementById('denunciaForm').addEventListener('submit', function(e) {
  e.preventDefault();

  const denunciado = document.getElementById('denunciado').value;
  const descricao = document.getElementById('descricao').value;

  fetch('http://192.168.10.87:5000/api/denuncia', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ denunciado, descricao })
  })
  .then(response => {
    if (response.ok) {
      const sucesso = document.getElementById('mensagemSucesso');
      sucesso.classList.remove('hidden');
      document.getElementById('denunciaForm').reset();
      setTimeout(() => {
        sucesso.classList.add('hidden');
      }, 5000);
    }
  })
  .catch(error => console.error('Erro ao enviar denúncia:', error));
});
