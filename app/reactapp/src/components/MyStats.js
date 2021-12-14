import { Statistic, Row, Col, Button } from 'antd';
// import { useState } from 'react';

function MyStats(){

    // const { User, setUser } = useState(null);

    return (
        <div>
            <Row gutter={16}>
                <Col span={12}>
                <Statistic title="Users" value={5} />
                </Col>
                <Col span={12}>
                <Statistic title="Account Balance (CNY)" value={112893} precision={2} />
                <Button style={{ marginTop: 16 }} type="primary">
                    Configure
                </Button>
                </Col>
                <Col span={12}>
                <Statistic title="Active Users" value={2} loading />
                </Col>
            </Row>
        </div>
    )
}
export default MyStats;