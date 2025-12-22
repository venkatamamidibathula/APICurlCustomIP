import streamlit as st
import subprocess
import shlex
import socket

st.title("🔗 API test with curl command .....")

ip = st.text_input("IP Address (leave empty for DNS lookup)", value="")
dns = st.text_input("DNS Name", value="")
curl_cmd = st.text_area("Curl Command", value="", height=100)

if st.button("🚀 Run Curl via Docker", type="primary"):
    if dns and curl_cmd:
        # Resolve IP if not provided
        resolved_ip = ip.strip()
        if not resolved_ip:
            try:
                resolved_ip = socket.gethostbyname(dns)
                st.info(f"🔍 DNS resolved {dns} → {resolved_ip}")
            except socket.gaierror:
                st.error(f"❌ Cannot resolve DNS: {dns}")
                st.stop()

        full_cmd = f"docker run --rm curl-hosts {shlex.quote(resolved_ip)} {shlex.quote(dns)} {shlex.quote(curl_cmd)}"

        st.code(f"`{full_cmd}`", language="bash")

        with st.spinner("Spinning up container..."):
            try:
                result = subprocess.run(full_cmd, shell=True, capture_output=True, text=True, timeout=30)

                st.subheader("**Response**")
                if result.returncode == 0:
                    st.success("✅ Success")
                    st.code(result.stdout)
                else:
                    st.error("❌ Failed")
                    st.code(result.stderr or result.stdout)

            except subprocess.TimeoutExpired:
                st.error("⏱️ Timeout")
            except Exception as e:
                st.error(f"💥 {str(e)}")
    else:
        st.warning("Fill DNS and Curl Command")
