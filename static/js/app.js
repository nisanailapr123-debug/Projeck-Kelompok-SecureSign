// SignDoc — app.js

// Preview nama file saat dipilih
const fileInput = document.getElementById('fileInput');
const uploadZone = document.getElementById('uploadZone');

if (fileInput) {
    fileInput.addEventListener('change', function () {
        if (this.files.length > 0) {
            const file = this.files[0];
            const sizeKb = (file.size / 1024).toFixed(1);
            document.getElementById('fileName').textContent = file.name;
            document.getElementById('fileSize').textContent = `(${sizeKb} KB)`;
            document.getElementById('fileInfo').classList.remove('d-none');
        }
    });
}

// Drag & drop pada upload zone
if (uploadZone) {
    uploadZone.addEventListener('dragover', (e) => {
        e.preventDefault();
        uploadZone.classList.add('bg-primary', 'bg-opacity-10');
    });

    uploadZone.addEventListener('dragleave', () => {
        uploadZone.classList.remove('bg-primary', 'bg-opacity-10');
    });

    uploadZone.addEventListener('drop', (e) => {
        e.preventDefault();
        uploadZone.classList.remove('bg-primary', 'bg-opacity-10');
        const file = e.dataTransfer.files[0];
        if (file && fileInput) {
            const dt = new DataTransfer();
            dt.items.add(file);
            fileInput.files = dt.files;
            fileInput.dispatchEvent(new Event('change'));
        }
    });

    // Klik pada zona upload
    uploadZone.addEventListener('click', (e) => {
        if (e.target.tagName !== 'BUTTON') {
            fileInput && fileInput.click();
        }
    });
}

// Auto-dismiss alert setelah 5 detik
document.querySelectorAll('.alert.alert-success, .alert.alert-info').forEach(alert => {
    setTimeout(() => {
        const bsAlert = bootstrap.Alert.getOrCreateInstance(alert);
        bsAlert && bsAlert.close();
    }, 5000);
});
