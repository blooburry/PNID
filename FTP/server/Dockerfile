FROM debian:latest

# Install FTP server and required tools
RUN apt-get update && apt-get install -y \
    vsftpd \
    libpam-pwquality \
    passwd \
    && rm -rf /var/lib/apt/lists/*

# Configure vsftpd
RUN echo "listen=YES" > /etc/vsftpd.conf && \
    echo "pasv_enable=YES" >> /etc/vsftpd.conf && \
    echo "pasv_min_port=30000" >> /etc/vsftpd.conf && \
    echo "pasv_max_port=30009" >> /etc/vsftpd.conf && \
    echo "pasv_address=192.168.178.76" >> /etc/vsftpd.conf\
    echo "anonymous_enable=NO" >> /etc/vsftpd.conf && \
    echo "local_enable=YES" >> /etc/vsftpd.conf && \
    echo "write_enable=YES" >> /etc/vsftpd.conf && \
    echo "secure_chroot_dir=/var/run/vsftpd/empty" >> /etc/vsftpd.conf

# Create the secure chroot directory
RUN mkdir -p /var/run/vsftpd/empty && chmod 755 /var/run/vsftpd/empty

# Add FTP users and set passwords
COPY create-users.sh /usr/local/bin/create-users.sh
RUN chmod +x /usr/local/bin/create-users.sh

# Expose ports
EXPOSE 21 30000-30009

# Start the vsftpd server
CMD ["/usr/local/bin/create-users.sh", "/usr/sbin/vsftpd", "/etc/vsftpd.conf"]