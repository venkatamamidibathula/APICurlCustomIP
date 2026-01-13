## 🎯 Problem
**Production outages in complex microservices** behind 4-node load balancers make it **impossible to pinpoint failing API endpoints**. 

**Current Pain Points:**
- Multiple rounds of hosts file updates required
- Admin privileges needed for `/etc/hosts` changes  
- DNS resolution masks the failing node
- Intermittent failures hard to reproduce consistently

## 💡 Solution  
**APICurlCustomIP** bypasses load balancers by letting you **directly target specific nodes** via IP address through a secure web UI.

**Key Benefits:**
- ✅ **No hosts file changes** - just enter IP in browser
- ✅ **No admin privileges** required
- ✅ **Instant DNS-to-IP resolution** 
- ✅ **Docker sandbox** for safe curl execution
- ✅ **Clear stdout/stderr** separation for debugging

**Result:** Identify the **exact failing node** in seconds, not hours.
