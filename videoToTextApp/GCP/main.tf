resource "google_compute_instance" "web" {
  name         = "web-instance"
  machine_type = "e2-standard-4"
  zone         = "us-central1-a"
  boot_disk {
    initialize_params {
      image = "fedora-cloud/fedora-39"
    }
  }
  network_interface {
    network = "default"
    access_config {}
  }
}